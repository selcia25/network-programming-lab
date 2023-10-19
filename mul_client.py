import socket
import threading

SERVER_HOST = socket.gethostname()
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print('[*] An error occurred while receiving messages.')
            client_socket.close()
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input()
    client_socket.send(message.encode('utf-8'))
