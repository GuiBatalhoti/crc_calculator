import socket
from crc import CRCCalc

class Client:
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
    

    def send(self, message):
        #send message to the addr
        self.sock.send(message)


def main():

    client = Client('localhost', 8000)

    while True:
        #user message
        message = input("Enter message: ")

        #calculate crc
        crc = CRCCalc(message)

        #sending message
        client.send(crc)

        #sent messagem
        print(f"Sent message: {crc}")
        
        #message recieved
        message_recv = client.recieve()
        print(f"Recieved message: {message_recv}")

        #code to see if user qant to exit program
        choice = input("Exit program? [Y]es or [N]no: ")
        if(choice.upper() == 'YES' or choice == "Y"):
            print("Exiting program...")
            client.close
            break
    