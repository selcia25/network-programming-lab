import time

class Router:
    def __init__(self, ip_address, name):
        self.ip_address = ip_address
        self.name = name

    def ping(self, target_ip):
        print(f"PING {target_ip} from {self.name} ({self.ip_address})")
        time.sleep(0.5)  # Simulated delay
        print(f"Reply from {target_ip}")

    def traceroute(self, target_ip):
        print(f"TRACEROUTE to {target_ip} from {self.name} ({self.ip_address})")
        hops = []
        current_router = self

        while current_router.ip_address != target_ip:
            hops.append(current_router.ip_address)
            time.sleep(0.5)  # Simulated delay

            # Simulate routing logic
            if current_router.ip_address == "192.168.1.1":
                next_router = Router("192.168.1.2", "Router 1")
            elif current_router.ip_address == "192.168.1.2":
                next_router = Router("192.168.1.3", "Router 2")
            elif current_router.ip_address == "192.168.1.3":
                next_router = Router("192.168.1.4", "Router 3")
            else:
                next_router = Router(target_ip, "Destination")

            current_router = next_router

        hops.append(current_router.ip_address)
        print("Trace complete.")
        print("Hops:")
        print(" -> ".join(hops))

# Create routers
router1 = Router("192.168.1.1", "Router 1")
router2 = Router("192.168.1.2", "Router 2")
router3 = Router("192.168.1.3", "Router 3")
destination_router = Router("192.168.1.4", "Destination")

# Perform PING
router1.ping("192.168.1.1")

# Perform TRACEROUTE
router1.traceroute("192.168.1.4")
