#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port. """    
    port = input("Enter a port: ")
    while True:
        print("Port is " + str(port))
        port = input("Enter a port: ")
