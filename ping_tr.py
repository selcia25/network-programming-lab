import socket
import time

def simulate_ping(target_host):
    target_ip = socket.gethostbyname(target_host)
    icmp = socket.getprotobyname('icmp')

    with socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp) as sock:
        # Set the timeout for receiving a response
        sock.settimeout(1)
        
        # Send the ping request
        sock.sendto(b'\x08\x00\x7d\x4b\x00\x00\x00\x00', (target_ip, 0))
        start_time = time.time()

        try:
            # Receive the ping response
            _, addr = sock.recvfrom(1024)
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
            print(f"Reply from {addr[0]}: time={elapsed_time:.2f}ms")
        except socket.timeout:
            print("Request timed out")

# Usage example
simulate_ping("example.com")
