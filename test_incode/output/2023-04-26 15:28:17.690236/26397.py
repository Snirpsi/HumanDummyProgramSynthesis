#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port or multiplyes user input. """    
    port = int(input("Enter a port number: "))
    multiplier = int(input("Enter a multiplier number: "))
    
    if port > 0 and port < 65535:
        