import socket

HOST = socket.gethostname()
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    filename = input('Enter filename: ')
    s.sendall(filename.encode())
    with open(filename, 'rb') as f:
        while True:
            data = f.read()
            if not data:
                break
            s.sendall(data)
    print(f'File {filename} sent successfully!')