import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 3000

client_socket.connect((host, port))
print(f"Đã kết nối tới {host}:{port}")

while True:
    message = input("Nhập chuỗi: ")

    client_socket.send(message.encode())

    data = client_socket.recv(1024)

    print("Nhận từ server:", data.decode())

client_socket.close()
