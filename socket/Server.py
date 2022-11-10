#importing socket and the crc calculator
import socket
from crc import CRCCalc


class Server:
    def __init__(self, host_addr, port) -> None:
        #socket ip host and port
        self.host_addr = host_addr
        self.port = port
        #initializing socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #biding socket to parameters
        self.sock.bind((self.host_addr, self.port))

    
    def close(self):
        #close the socket
        self.sock.close()

    
    def recieve(self):
        #recieve message
        return self.sock.recvfrom(1024)
    

    def send(self, message, dest_addr):
        #send message to the addr
        self.sock.sendto(message, dest_addr)
    

def main():
    #creating the server
    server = Server('localhost', 8000)

    try:
        while True:
            #getting message and address
            message, dest_addr = server.recieve()
            print(f"Recieved message: {message}")

            crc = CRCCalc(data = message)

            server.send(crc, dest_addr)
            print(f"Sent message: {crc}")
    
    except KeyboardInterrupt:
        print("Server closed")
        server.close()
        exit(1)


if __name__ == '__main__':
    main()