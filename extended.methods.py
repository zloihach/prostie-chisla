import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


class PrimeNumberUtils:
    prime_cache = {}

    @staticmethod
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def sieve_of_eratosthenes(limit: int) -> list:
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for num in range(2, int(limit ** 0.5) + 1):
            if sieve[num]:
                for i in range(num * num, limit + 1, num):
                    sieve[i] = False
        return [i for i, is_prime in enumerate(sieve) if is_prime]

    @staticmethod
    def nth_prime(n: int) -> int:
        count = 0
        num = 1
        while count < n:
            num += 1
            if PrimeNumberUtils.is_prime(num):
                count += 1
        return num

    @staticmethod
    def prime_factors(n: int) -> list:
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n > 2:
            factors.append(n)
        return factors

    @staticmethod
    def primes_between(start: int, end: int) -> list:
        return [num for num in range(start, end + 1) if PrimeNumberUtils.is_prime(num)]


# Интерфейс на tkinter
class PrimeNumberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prime Number Utils")

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
            if PrimeNumberUtils.is_prime(n):
                messagebox.showinfo("Результат", f"Число {n} является простым.")
            else:
                messagebox.showinfo("Результат", f"Число {n} не является простым.")

    def generate_primes(self):
        limit = simpledialog.askinteger("Простые до N", "Введите предел:")
        if limit is not None:
            primes = PrimeNumberUtils.sieve_of_eratosthenes(limit)
            messagebox.showinfo("Простые числа", f"Простые числа до {limit}: {primes}")

    def get_nth_prime(self):
        n = simpledialog.askinteger("N-е простое число", "Введите N:")
        if n is not None:
            nth_prime = PrimeNumberUtils.nth_prime(n)
            messagebox.showinfo("Результат", f"{n}-е простое число: {nth_prime}")

    def get_prime_factors(self):
        n = simpledialog.askinteger("Простые множители", "Введите число для факторизации:")
        if n is not None:
            factors = PrimeNumberUtils.prime_factors(n)
            messagebox.showinfo("Результат", f"Простые множители числа {n}: {factors}")

    def get_primes_between(self):
        start = simpledialog.askinteger("Начало диапазона", "Введите начальное число:")
        end = simpledialog.askinteger("Конец диапазона", "Введите конечное число:")
        if start is not None and end is not None:
            primes = PrimeNumberUtils.primes_between(start, end)
            messagebox.showinfo("Простые числа", f"Простые числа между {start} и {end}: {primes}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PrimeNumberApp(root)
    root.mainloop()
