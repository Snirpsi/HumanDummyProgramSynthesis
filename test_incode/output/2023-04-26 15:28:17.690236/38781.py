#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports or iterates over numbers. """    
    while True:
        port = int(input("Enter a port number: "))
        if port > 65535:
            print("Port number must be less than 65535.")
        else:
            print(