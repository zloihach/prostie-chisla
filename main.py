class PrimeNumberUtils:
    @staticmethod
    def is_prime(n: int) -> bool:
        """Проверяет, является ли число простым."""
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
    def generate_primes(limit: int) -> list:
        """Генерирует список простых чисел до указанного предела."""
        primes = []
        for num in range(2, limit + 1):
            if PrimeNumberUtils.is_prime(num):
                primes.append(num)
        return primes

    @staticmethod
    def nth_prime(n: int) -> int:
        """Возвращает n-е простое число."""
        count = 0
        num = 1
        while count < n:
            num += 1
            if PrimeNumberUtils.is_prime(num):
                count += 1
        return num

    @staticmethod
    def prime_factors(n: int) -> list:
        """Возвращает список простых множителей числа."""
        factors = []
        # Делим число на 2, пока оно четное
        while n % 2 == 0:
            factors.append(2)
            n //= 2

        # Проходим по нечетным числам начиная с 3
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i

        # Если число осталось простым и больше 2
        if n > 2:
            factors.append(n)
        return factors

    @staticmethod
    def primes_between(start: int, end: int) -> list:
        """Возвращает список простых чисел в заданном диапазоне."""
        return [num for num in range(start, end + 1) if PrimeNumberUtils.is_prime(num)]


# Пример использования модуля
if __name__ == "__main__":
    print("Проверка, что 17 - простое число:", PrimeNumberUtils.is_prime(17))
    print("Простые числа до 50:", PrimeNumberUtils.generate_primes(50))
    print("5-е простое число:", PrimeNumberUtils.nth_prime(5))
    print("Простые множители числа 100:", PrimeNumberUtils.prime_factors(100))
    print("Простые числа между 10 и 30:", PrimeNumberUtils.primes_between(10, 30))
