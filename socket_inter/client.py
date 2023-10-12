import socket
import threading

HOST = '127.0.0.1'
PORT = 3434

def client_thread():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    data = s.recv(1024)
    print(data)

    s.close()

# 创建十个线程
threads = []
for _ in range(100):
    thread = threading.Thread(target=client_thread)
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()