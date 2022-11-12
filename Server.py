#importing socket and the crc calculator
import socket
from CRCCalc import decodeMessage


generator = '100000111'


def main():
    #creating the TCP server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8000))
    print("Server started.")
    server.listen()
    print("Waiting for conection...")

    #getting message and address
    server.listen()
    conection, client = server.accept()
    
    #recieving message with 1024 bytes
    message = conection.recv(1024)

    #pinting the recived messages
    print("Message recieved in binary:", message.decode())
    
    #decoding the messade
    division_result = decodeMessage(message, generator)
    
    aux = '0' * (len(generator) - 1)
    #checking message
    if division_result == aux:
        print("The message is correct!!!! :)")
    else:
        print("The message is incorrect... :(")

    print("Server closed...")
    server.close()


if __name__ == '__main__':
    main()