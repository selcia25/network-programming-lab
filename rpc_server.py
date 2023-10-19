import socket
import threading

def add(a, b):
    return int(a) + int(b)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = socket.gethostname()
server_port = 12347
server_socket.bind((server_ip, server_port))
server_socket.listen(5)
print(f"RPC Server listening on {server_ip}:{server_port}")
def handle_client(client_socket):
    while True:
        request = client_socket.recv(1024).decode().split()
        if not request:
            break
        if len(request)!=3:
            print("Invalid request")
        method = request[0]
        x = request[1]
        y = request[2]
        if method == 'ADD':
            client_socket.sendall(str(add(x, y)).encode())
        if request[1] == 'QUIT':
            break

while True:
    client_socket, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
server_socket.close()