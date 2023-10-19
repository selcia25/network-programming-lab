import socket

# Define server host and port
HOST = '127.0.0.1'
PORT = 5000

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # Bind the socket object to the host and port
    s.bind((HOST, PORT))
    print(f"Server started on {HOST}:{PORT}")

    while True:
        # Receive data from the client
        data, addr = s.recvfrom(1024)
        print(f"Received data from {addr}: {data.decode()}")
        # Send the data back to the client
        s.sendto(data, addr)
        break