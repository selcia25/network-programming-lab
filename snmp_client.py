from twisted.internet import reactor, protocol
import socket


class SNMPClientProtocol(protocol.DatagramProtocol):
    def startProtocol(self):
        ip_address = socket.gethostbyname("localhost")
        self.transport.connect(ip_address, 8888)
        self.sendRequest()

    def sendRequest(self):
        self.transport.write("SNMP GET request".encode())

    def datagramReceived(self, data, addr):
        print("Received data:", data.decode())
        # Process the received SNMP response
        reactor.stop()


if __name__ == "__main__":
    reactor.listenUDP(0, SNMPClientProtocol())
    reactor.callLater(1, reactor.stop)  # Stop reactor after 1 second
    reactor.run()