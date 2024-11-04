class PrimeNumberUtils:
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


def main():
    # Проверка, является ли число простым
    number = 29
    print(f"Число {number} простое? {PrimeNumberUtils.is_prime(number)}")

    # Нахождение всех простых чисел до заданного предела
    limit = 50
    print(f"Простые числа до {limit}: {PrimeNumberUtils.sieve_of_eratosthenes(limit)}")

    # Нахождение n-го простого числа
    nth = 10
    print(f"{nth}-е простое число: {PrimeNumberUtils.nth_prime(nth)}")

    # Разложение числа на простые множители
    number_to_factor = 84
    print(f"Простые множители числа {number_to_factor}: {PrimeNumberUtils.prime_factors(number_to_factor)}")

    # Нахождение простых чисел в заданном диапазоне
    start, end = 10, 30
    print(f"Простые числа в диапазоне от {start} до {end}: {PrimeNumberUtils.primes_between(start, end)}")


if __name__ == "__main__":
    main()
