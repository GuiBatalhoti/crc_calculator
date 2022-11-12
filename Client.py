import socket
from CRCCalc import encodeMessage

generator = '100000111'


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 8000))
    print("Client connected...")
    #user message
    print(f"The message to be sent is 'hey'.")

    # the message is 'hey' -> in hex is 0x686579
    # 'h' is 0x68 | 'e' is 0x65 | 'y' -> 0x79
    message = 0x686579
    message = bin(message)[2:]
    print("The binary messsage is:", message)

    #enconding and sen sending data
    division_result = encodeMessage(message, generator)
    print("The encoded data is:", division_result)

    client.send(division_result.encode())
    print("Data just sent!! :)")
    client.close()

if __name__ == '__main__':
    main()
    