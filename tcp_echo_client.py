import socket

# Define the IP address and the port number of the server
HOST = socket.gethostname()
PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Receive the message from the server
data = client_socket.recv(1024).decode()
print(f"Received message from server: {data}")

# Send a message to the server
message = input("Send message to server: ")
client_socket.send(message.encode())

# Close the connection
client_socket.close()

# This client program connects to a specified IP address and port number, and waits to receive a message from the server. 
# Once it receives the message, it sends a response to the server and closes the connection.