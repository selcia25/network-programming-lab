import socket

# Define the IP address and the port number that the socket will listen on
HOST = 'localhost'
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

# Define the data to be sent
data = "Hey Selcia"

# Send the data
client_socket.send(data.encode())

# Receive the acknowledgement
ack = client_socket.recv(1024)

# Print the acknowledgement
if not ack:
    print("Error: Empty acknowledgement message received")
else:
    # Print the acknowledgement
    print(f"Acknowledgement received: {ack.decode()}")

# Close the connection
client_socket.close()
server_socket.close()
