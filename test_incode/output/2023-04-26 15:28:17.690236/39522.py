#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a port or calculates a port. """    
    port = int(input("Enter a port number: "))
    if port < 0 or port > 65535:
        print("Port number must be between 0 and 65535.")
    else:
        print("The port number is " + str(port))
    
