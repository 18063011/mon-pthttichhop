import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 3000

server_socket.bind((host, port))

server_socket.listen(1)
print(f"Server đang lắng nghe trên {host}:{port}...")

client_socket, client_address = server_socket.accept()
print(f"Kết nối từ {client_address} đã được chấp nhận.")

while True:
    data = client_socket.recv(1024)
    if not data:
        break

    uppercase_data = data.decode().upper()

    client_socket.send(uppercase_data.encode())

# Đóng kết nối
client_socket.close()
server_socket.close()
