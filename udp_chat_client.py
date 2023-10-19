import socket

# Define server host and port
HOST = '127.0.0.1'
PORT = 65432

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        # Get message to send from user input
        message = input("Enter message: ")

        # Send message to server
        s.sendto(message.encode(), (HOST, PORT))
        if message == "exit":
            break
        # Receive response from server
        data, addr = s.recvfrom(1024)
        print(f"Received response from {addr}: {data.decode()}")
    s.close()