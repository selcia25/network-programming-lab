import socket

def send_request(sock, request):
    sock.sendall(request.encode())
    response = sock.recv(1024).decode()
    print('Response:', response)

def connect_to_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((socket.gethostname(), 12347))  # Replace with the appropriate server IP and port
    return sock

def prompt_loop(sock):
    while True:
        request = input('Enter request (ADD/SUB/MUL/DIV x y): ')

        if request == 'QUIT':
            break

        send_request(sock, request)

    sock.close()

if __name__ == '__main__':
    client_socket = connect_to_server()
    prompt_loop(client_socket)
