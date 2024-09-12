from xmlrpc.server import SimpleXMLRPCServer
import prime_lib  # Импортируем скомпилированный C-модуль

# Создаем сервер
server = SimpleXMLRPCServer(("localhost", 8000))
print("Сервер запущен на порту 8000...")

# Регистрируем методы, реализованные в C
server.register_function(prime_lib.is_prime, "is_prime")
server.register_function(prime_lib.sieve_of_eratosthenes, "sieve_of_eratosthenes")
server.register_function(prime_lib.nth_prime, "nth_prime")
server.register_function(prime_lib.prime_factors, "prime_factors")

# Запуск сервера
server.serve_forever()
