import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 9999

# connect to the server
client_socket.connect((host, port))

while True:
    # send message to server
    message = input("Client:")
    client_socket.send(message.encode('utf-8'))

    # check for exit command
    if message == 'exit':
        break

    # receive response from server
    data = client_socket.recv(1024).decode('utf-8')

    # print response
    print("Server:", data)

# close the connection
client_socket.close()