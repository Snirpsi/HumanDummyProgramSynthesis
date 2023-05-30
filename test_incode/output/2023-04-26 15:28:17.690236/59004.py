#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or converts fruits. """    
    while True:
        port = int(input("Enter a port number: "))
        if port > 65535:
            print("Error: Port number must be between 1 and 65535.")
        elif port < 1:
            print("Error: Port number must be between 1 and 65535.")
        else:
            print("Port: ", port)
            fruits = input("Enter a fruit name: ")
            if fruits == '':
                print("Error: Please enter a fruit name.")
            else:
                print("Fruit: ", fruits)
                fruits_