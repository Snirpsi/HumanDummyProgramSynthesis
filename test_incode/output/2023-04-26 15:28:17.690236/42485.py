#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port. """    
    port = int(input("Enter the port number: "))
    
    if port < 0 or port > 65535:
        print("Port number must be between 0 and 65535.")
    else:
        print("The port number is", port)
    
