#importing socket and the crc calculator
import socket
# from crc_calc import CRCCalc   

def main():
    #creating the TCP server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server started.")
    server.listen()
    print("Waiting for conection...")

    try:
        while True:
            #getting message and address
            server.listen()
            conection, client = server.accept()
            
            message = server.recv()
            print(message)
    
    except KeyboardInterrupt:
        print("Server closed")
        server.close()
        exit(1)


if __name__ == '__main__':
    main()