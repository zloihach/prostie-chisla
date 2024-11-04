# run.py
import threading
import subprocess
import time

def start_server():
    subprocess.run(["python", "l3-server.py"])

def start_client():
    time.sleep(1)  # Небольшая задержка, чтобы сервер успел запуститься
    subprocess.run(["python", "l3-client.py"])

if __name__ == "__main__":
    # Запуск сервера в отдельном потоке
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # Запуск клиента
    start_client()

    # Ожидание завершения потока сервера
    server_thread.join()
