#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or multiplyes user input. """    
    while True:
        print("Enter a port number:")
        port = int(input())
        
        if port % 2 == 0:
            print("The port number is even.")
        else:
            print("The port number is odd.")
