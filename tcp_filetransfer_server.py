import socket
# Define server host and port
HOST = socket.gethostname()
PORT = 65432

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket object to the host and port
    s.bind((HOST, PORT))
    print(f"Server started on {HOST}:{PORT}")
    # Listen for incoming connections
    s.listen()
   
    # Accept incoming connection
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    with conn:
        # Receive file name from the client
        filename = conn.recv(1024).decode()
        # Open the file for writing
        with open("file2.txt", 'wb') as f:
            # Receive data from the client and write it to the file
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
        print(f"File {filename} received successfully!")
        with open(filename, 'r') as f:
            file_contents = f.read()
            print(f"Contents of file {filename}: {file_contents}")
