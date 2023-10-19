import time
class ARP:
    def __init__(self):
        self.cache = {}   # ARP cache to store MAC address and IP address mappings
    def add_mapping(self, ip_address, mac_address):
        self.cache[ip_address] = mac_address
    def lookup(self, ip_address):
        if ip_address in self.cache:
            return self.cache[ip_address]
        else:
            return None
class Device:
    def __init__(self, name, ip_address, mac_address):
        self.name = name
        self.ip_address = ip_address
        self.mac_address = mac_address
    def send(self, destination_ip_address):
        print(f"{self.name} sending packet to {destination_ip_address}")
        destination_mac_address = arp.lookup(destination_ip_address)
        if destination_mac_address is not None:
            print(f"{self.name} found MAC address {destination_mac_address} for IP address {destination_ip_address}")
            print(f"{self.name} sending packet to {destination_mac_address}")
            time.sleep(1)   # simulate network delay
            print(f"{self.name} packet sent")
        else:
            print(f"{self.name} could not find MAC address for IP address {destination_ip_address}")
arp = ARP()   # create an instance of the ARP cache
# create two devices
device1 = Device("Device 1", "192.168.1.1", "00:11:22:33:44:55")
device2 = Device("Device 2", "192.168.1.2", "AA:BB:CC:DD:EE:FF")

# add mappings to the ARP cache
arp.add_mapping(device1.ip_address, device1.mac_address)
arp.add_mapping(device2.ip_address, device2.mac_address)

# simulate a packet being sent from device1 to device2
device1.send(device2.ip_address)


'''In this simulation, we have two devices, device1 and device2, each with an IP address and MAC address. 
We also have an instance of an ARP cache, arp, which is initially empty.

The Device class has a send method which simulates sending a packet to a specified IP address. The method first looks up the MAC address for the destination IP address in the ARP cache. If the MAC address is found, the packet is sent to the destination MAC address. Otherwise, the method prints an error message indicating that the MAC address could not be found.

To add mappings to the ARP cache, we use the add_mapping method of the ARP class. This method takes an IP address and a MAC address and adds them to the cache.

In the example code, we add mappings for device1 and device2 to the ARP cache, and then simulate a packet being sent from device1 to device2. The output of running the code should look something like this:'''