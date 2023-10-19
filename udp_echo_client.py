import socket

# Define server host and port
HOST = '127.0.0.1'
PORT = 5000

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # Get the message to send from user input
    message = input("Enter a message to send to the server: ")

    # Send the message to the server
    s.sendto(message.encode(), (HOST, PORT))

    # Receive the response from the server
    response, addr = s.recvfrom(1024)
    print(f"Received response from {addr}: {response.decode()}")
