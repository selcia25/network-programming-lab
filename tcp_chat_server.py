import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 9999

# bind the socket to a public host, and a port
server_socket.bind((host, port))

# queue up to 5 requests
server_socket.listen(5)

# wait for a connection
print("Waiting for connection...")
client_socket, addr = server_socket.accept()
print("Connection established with", addr)

while True:
    # receive data from client
    data = client_socket.recv(1024).decode('utf-8')

    # print received message
    print("Client:", data)

    # send response to client
    message = input("Server:")
    client_socket.send(message.encode('utf-8'))

    # check for exit command
    if message == 'exit':
        break

# close the connection
client_socket.close()
server_socket.close()
