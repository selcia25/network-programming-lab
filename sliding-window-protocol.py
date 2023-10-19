import socket

# Define the IP address and the port number that the socket will listen on
HOST = 'localhost'
PORT = 34561

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
data = "Hello, world!"
data_bytes = data.encode()

# Define the window size and the base sequence number
window_size = 3
base_sequence_number = 0

# Send the packets in the window
while base_sequence_number < len(data_bytes):
    for i in range(base_sequence_number, min(base_sequence_number + window_size, len(data_bytes))):
        packet = data_bytes[i:i+1]
        client_socket.send(packet)

    # Receive the acknowledgement
    ack = client_socket.recv(1024)

    # Check if the acknowledgement message is empty
    if not ack:
        print("Error: Empty acknowledgement message received")
        break

    # Print the acknowledgement
    print(f"Acknowledgement received: {ack.decode()}")

    # Update the base sequence number based on the acknowledgement received
    base_sequence_number = int(ack.decode())

# Close the connection
client_socket.close()
server_socket.close()
