#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers or stores a port. """    
    while True:
        port = int(input("Enter a port: "))
        if port < 1 or port > 65535:
            print("Invalid port. Try again.")
        else:
            print("Opening port ", port)
            