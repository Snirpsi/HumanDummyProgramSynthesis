#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or iterates over a port. """    
    port = input("Enter a port to listen to: ")
    while True:
        print(port)
        port = input("Enter a port to listen to: ")
