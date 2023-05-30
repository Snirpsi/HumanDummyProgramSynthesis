#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers and opens a port. """    
    while True:
        port = int(input("Enter a port number: "))
        print("Opening port: ", port)
        