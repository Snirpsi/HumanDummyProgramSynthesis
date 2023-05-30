#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port and returns a port. """    
    port = int(input("Enter a port number: "))
    
    multiplier = int(input("Enter a multiplier: "))
    
    port = (port * multiplier)
    
    print("The port multiplied by {} is {}".format(multiplier, port))
    
