#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input or returns a port. """    
    while True:
        port = int(input("Enter a port number to multiply by: "))
        if port > 65535:
            print("Port number too large for multiplication")
        else:
            print("The port multiplied by " + str(port) + " is: " + str(port * 