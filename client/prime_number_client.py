from tkinter import simpledialog, messagebox
import xmlrpc.client

import tk

# Подключаемся к серверу XML-RPC
server = xmlrpc.client.ServerProxy("http://localhost:8000")

class PrimeNumberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prime Number Utils (Client)")

        self.label = tk.Label(root, text="Выберите операцию:")
        self.label.pack(pady=10)

        self.is_prime_btn = tk.Button(root, text="Проверить простоту числа", command=self.check_prime)
        self.is_prime_btn.pack(pady=5)

        self.primes_up_to_btn = tk.Button(root, text="Простые числа до N", command=self.generate_primes)
        self.primes_up_to_btn.pack(pady=5)

        self.nth_prime_btn = tk.Button(root, text="Н-е простое число", command=self.get_nth_prime)
        self.nth_prime_btn.pack(pady=5)

        self.prime_factors_btn = tk.Button(root, text="Простые множители числа", command=self.get_prime_factors)
        self.prime_factors_btn.pack(pady=5)

        self.primes_between_btn = tk.Button(root, text="Простые числа в диапазоне", command=self.get_primes_between)
        self.primes_between_btn.pack(pady=5)

    def check_prime(self):
        n = simpledialog.askinteger("Проверка простоты", "Введите число для проверки:")
        if n is not None:
            result = server.is_prime(n)
            if result:
                messagebox.showinfo("Результат", f"Число {n} является простым.")
            else:
                messagebox.showinfo("Результат", f"Число {n} не является простым.")

    def generate_primes(self):
        limit = simpledialog.askinteger("Простые до N", "Введите предел:")
        if limit is not None:
            primes = server.sieve_of_eratosthenes(limit)
            messagebox.showinfo("Простые числа", f"Простые числа до {limit}: {primes}")

    def get_nth_prime(self):
        n = simpledialog.askinteger("N-е простое число", "Введите N:")
        if n is not None:
            nth_prime = server.nth_prime(n)
            messagebox.showinfo("Результат", f"{n}-е простое число: {nth_prime}")

    def get_prime_factors(self):
        n = simpledialog.askinteger("Простые множители", "Введите число для факторизации:")
        if n is not None:
            factors = server.prime_factors(n)
            messagebox.showinfo("Результат", f"Простые множители числа {n}: {factors}")

    def get_primes_between(self):
        start = simpledialog.askinteger("Начало диапазона", "Введите начальное число:")
        end = simpledialog.askinteger("Конец диапазона", "Введите конечное число:")
        if start is not None and end is not None:
            primes = server.primes_between(start, end)
            messagebox.showinfo("Простые числа", f"Простые числа между {start} и {end}: {primes}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PrimeNumberApp(root)
    root.mainloop()
