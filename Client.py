import socket
from CRCCalc import mod2div


generator = 0x81


def main():
    #the message is 'hey' to be sent in bytes
    message = 0x686579
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        client.connect(('localhost', 8000))
        print("Client connected...")
        #user message
        print(f"The message to be sent is {message}.")

        message_with_zeros = message << 8
        dividend = mod2div(message_with_zeros, generator)
        bits_message = format(message, '016b') + format(dividend, '016b')

        client.send(int.to_bytes(int(bits_message, base=2), length=4, byteorder='big'))

        #code to see if user qant to exit program
        choice = input("Exit program? [Y]es or [N]no: ")
        if(choice.upper() == 'YES' or choice == "Y"):
            print("Exiting program...")
            client.close
            break


if __name__ == '__main__':
    main()
    