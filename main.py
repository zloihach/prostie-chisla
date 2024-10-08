import subprocess
import time

def start_server():
    # Запуск сервера в фоновом процессе
    return subprocess.Popen(['python', 'server/prime_number_server.py'])

def start_client():
    # Запуск клиента
    subprocess.run(['python', 'client/prime_number_client.py'])

if __name__ == "__main__":
    print("Запуск сервера...")
    server_process = start_server()

    time.sleep(2)

    print("Запуск клиента...")
    start_client()

    server_process.terminate()
