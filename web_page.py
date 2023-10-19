import socket

def send_http_request(host, port, request):
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect to the server
        sock.connect((host, port))

        # Send the HTTP request
        sock.sendall(request.encode())

        # Receive and print the response
        response = sock.recv(4096).decode()
        print(response)
    finally:
        # Close the socket
        sock.close()

# Example usage: 
print("Uploading a file to a web server using HTTP POST")

# Define the target server details
server_host = "example.com"
server_port = 80

# Define the HTTP request with file upload
request = (
    "POST /upload HTTP/1.1\r\n"
    "Host: example.com\r\n"
    "Content-Type: multipart/form-data; boundary=----WebKitFormBoundary\r\n"
    "\r\n"
    "------WebKitFormBoundary\r\n"
    "Content-Disposition: form-data; name=\"file\"; filename=\"example.txt\"\r\n"
    "Content-Type: text/plain\r\n"
    "\r\n"
    "This is an example file.\r\n"
    "------WebKitFormBoundary--\r\n"
)

# Send the HTTP request to upload the file
send_http_request(server_host, server_port, request)


# Example usage: 
print("Downloading a web page using HTTP GET")

# Define the target server details
server_host = "example.com"
server_port = 80

# Define the HTTP request for page download
request = (
    "GET /index.html HTTP/1.1\r\n"
    "Host: example.com\r\n"
    "\r\n"
)

# Send the HTTP request to download the web page
send_http_request(server_host, server_port, request)