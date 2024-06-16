import socket
import threading

HOST = '127.0.0.1'
PORT = 9090


def handle_client(conn, addr):
	print(f'Подключено от: {addr}')
	with conn:
		while True:
			data = conn.recv(1024)
			if not data:
				break
			message = data.decode()
			print(f"Получено от {addr}: {message}")
			conn.sendall(f"Echo: {message}".encode())


with socket.socket() as s:
	s.bind((HOST, PORT))
	s.listen()
	while True:
		conn, addr = s.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()

