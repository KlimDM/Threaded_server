import socket

HOST = '127.0.0.1'
PORT = 9090

with socket.socket() as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Введите сообщение: ")
        s.sendall(message.encode())
        data = s.recv(1024)
        print('Получено:', data.decode())
