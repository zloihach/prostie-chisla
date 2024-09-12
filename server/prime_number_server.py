from xmlrpc.server import SimpleXMLRPCServer
from server.prime_number_utils import PrimeNumberUtils

server = SimpleXMLRPCServer(("localhost", 8000), logRequests=True)
print("Сервер запущен на порту 8000...")

server.register_function(PrimeNumberUtils.is_prime, "is_prime")
server.register_function(PrimeNumberUtils.sieve_of_eratosthenes, "sieve_of_eratosthenes")
server.register_function(PrimeNumberUtils.nth_prime, "nth_prime")
server.register_function(PrimeNumberUtils.prime_factors, "prime_factors")
server.register_function(PrimeNumberUtils.primes_between, "primes_between")

server.serve_forever()
