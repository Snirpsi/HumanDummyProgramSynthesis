#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port or multiplyes a port. """    
    port = int(input("Enter a port number: "))
    
    if port % 2 == 0:
        print("The port number {} is even.".format(port))
    else:
        print("The port number {} is odd.".format(port))
    
