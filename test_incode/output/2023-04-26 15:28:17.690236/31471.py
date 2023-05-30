#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port or adds a port. """    
    while True:
        port = int(input("Enter a port number: "))
        multiplier = int(input("Enter a multiplier: "))
        
        if port > 0 and multiplier > 0:
            