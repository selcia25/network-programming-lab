import socket
import threading

host = socket.gethostname()
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(5)
print("Waiting for connection...")
client_sockets = []
client_usernames = []

def broadcast(message):
    for client_socket in client_sockets:
        client_socket.send(message.encode())

def handle_client(client_socket):
    while True:
        try:
            message =client_socket.recv(1024).decode()
            broadcast(message)
        except:
            client_sockets.remove(client_socket)
            client_socket.close()
            break

while True:
    client, address = server_socket.accept()
    print(f"[*] Accepted connection from {address[0]}:{address[1]}")
    client_sockets.append(client)
    client_thread = threading.Thread(target=handle_client, args=(client,))
    client_thread.start()