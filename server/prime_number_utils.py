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

