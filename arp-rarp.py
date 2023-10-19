import random

class ARP:
    def __init__(self, ip_address, mac_address):
        self.ip_address = ip_address
        self.mac_address = mac_address

class RARP:
    def __init__(self, ip_address, mac_address):
        self.ip_address = ip_address
        self.mac_address = mac_address

class ARPNetwork:
    def __init__(self):
        self.devices = {}

    def add_device(self, device):
        self.devices[device.ip_address] = device

    def arp_request(self, source_ip, target_ip):
        source_device = self.devices.get(source_ip)
        target_device = self.devices.get(target_ip)

        if source_device and target_device:
            print(f"ARP Request: {source_device.mac_address} ({source_device.ip_address}) requests MAC address for {target_device.ip_address}")
            return target_device.mac_address
        else:
            return None

class RARPNetwork:
    def __init__(self):
        self.devices = {}

    def add_device(self, device):
        self.devices[device.mac_address] = device

    def rarp_request(self, source_mac):
        source_device = self.devices.get(source_mac)

        if source_device:
            print(f"RARP Request: {source_device.ip_address} ({source_device.mac_address}) requests IP address")
            return source_device.ip_address
        else:
            return None

# Generate a random IP address
def generate_ip_address():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

# Generate a random MAC address
def generate_mac_address():
    mac_digits = [random.randint(0x00, 0xff) for _ in range(6)]
    mac_address = ":".join("{:02x}".format(digit) for digit in mac_digits)
    return mac_address

# ARP simulation
arp_network = ARPNetwork()

device1 = ARP(generate_ip_address(), generate_mac_address())
device2 = ARP(generate_ip_address(), generate_mac_address())
device3 = ARP(generate_ip_address(), generate_mac_address())

arp_network.add_device(device1)
arp_network.add_device(device2)
arp_network.add_device(device3)

source_ip = device1.ip_address
target_ip = device2.ip_address
mac_address = arp_network.arp_request(source_ip, target_ip)

if mac_address:
    print(f"ARP Response: MAC address {mac_address} received")

# RARP simulation
rarp_network = RARPNetwork()

device4 = RARP(generate_ip_address(), generate_mac_address())
device5 = RARP(generate_ip_address(), generate_mac_address())
device6 = RARP(generate_ip_address(), generate_mac_address())

rarp_network.add_device(device4)
rarp_network.add_device(device5)
rarp_network.add_device(device6)

source_mac = device5.mac_address
ip_address = rarp_network.rarp_request(source_mac)

if ip_address:
    print(f"RARP Response: IP address {ip_address} received")
