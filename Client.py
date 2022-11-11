import socket
from CRCCalc import CRCCalc


def main():
    #the message to be sent in bytes
    message = 'hey'.encode("hex")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        client.connect('localhost', 8000)
        print("Client connected...")
        #user message
        print(f"The message to be sent is {message.decode('ascii')}.")

        #calculate crc
        crc = CRCCalc(message)

        #sending message
        client.send(message)

        #code to see if user qant to exit program
        choice = input("Exit program? [Y]es or [N]no: ")
        if(choice.upper() == 'YES' or choice == "Y"):
            print("Exiting program...")
            client.close
            break


if __name__ == '__main__':
    main()
    