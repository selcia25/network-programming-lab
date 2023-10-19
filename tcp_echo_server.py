import socket

# Define the IP address and the port number that the socket will listen on
HOST = socket.gethostname()
PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and the port number
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

# Accept a connection
print('Waiting for a connection...')
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Send a message to the client
message = input("Send a message to client: ")
client_socket.send(message.encode())

# Receive a message from the client
data = client_socket.recv(1024).decode()
print(f"Received message from client: {data}")

# Close the connection
client_socket.close()
server_socket.close()

# This server program listens for incoming connections on a specified IP address and port number. 
# When a client connects, it sends a message to the client and waits for a response. 
# Once it receives a response from the client, it prints out the message and closes the connection.