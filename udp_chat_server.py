import socket

# Define server host and port
HOST = '127.0.0.1'
PORT = 65432

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # Bind the socket object to the host and port
    s.bind((HOST, PORT))
    print(f"Server started on {HOST}:{PORT}")

    while True:
        # Receive message from client
        data, addr = s.recvfrom(1024)
        print(f"Received message from {addr}: {data.decode()}")
        # Send message back to client
        response = input("Enter response: ")
        if response == 'exit':
            break
        s.sendto(response.encode(), addr)
