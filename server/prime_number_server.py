# server/prime_number_server.py
from xmlrpc.server import SimpleXMLRPCServer

from main import PrimeNumberUtils

# Создаем сервер XML-RPC
server = SimpleXMLRPCServer(("localhost", 8000), logRequests=True)
print("Сервер запущен на порту 8000...")

# Регистрируем функции для XML-RPC
server.register_function(PrimeNumberUtils.is_prime, "is_prime")
server.register_function(PrimeNumberUtils.sieve_of_eratosthenes, "sieve_of_eratosthenes")
server.register_function(PrimeNumberUtils.nth_prime, "nth_prime")
server.register_function(PrimeNumberUtils.prime_factors, "prime_factors")
server.register_function(PrimeNumberUtils.primes_between, "primes_between")

# Запуск сервера
server.serve_forever()
