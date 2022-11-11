#importing socket and the crc calculator
import socket
from CRCCalc import is_valid_crc  


generator = 0x81


def main():
    #creating the TCP server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8000))
    print("Server started.")
    server.listen()
    print("Waiting for conection...")

    try:
        while True:
            #getting message and address
            server.listen()
            conection, client = server.accept()
            
            #recieving message
            message_rcv_with_checksum = conection.recv(4)
            #spliting the message and checksum
            message_rcv = message_rcv_with_checksum[0:3]
            checksum = message_rcv_with_checksum[3:4]

            #pinting the recived messages
            print(f"Message recieved:", message_rcv)
            print(f"Checksum recieved:", checksum)

            #checking message
            if is_valid_crc(message_rcv_with_checksum):
                print("The message is correct!!!! :)")
            else:
                print("The message is incorrect... :(")
  
    except KeyboardInterrupt:
        print("Server closed...")
        server.close()
        exit(1)


if __name__ == '__main__':
    main()