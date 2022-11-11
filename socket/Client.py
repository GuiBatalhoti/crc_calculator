import socket
# from crc_calc import CRCCalc


def main():

    client = Client('localhost', 8000)

    while True:
        #user message
        message = input("Enter message: ")

        #calculate crc
        # crc = CRCCalc(message)

        #sending message
        client.send(message)

        #sent messagem
        print(f"Sent message: {message}")
        
        #message recieved
        message_recv = client.recieve()
        print(f"Recieved message: {message_recv}")

        #code to see if user qant to exit program
        choice = input("Exit program? [Y]es or [N]no: ")
        if(choice.upper() == 'YES' or choice == "Y"):
            print("Exiting program...")
            client.close
            break


if __name__ == '__main__':
    main()
    