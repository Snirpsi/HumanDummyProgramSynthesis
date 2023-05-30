#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port or prints a port. """    
    while True:
        port = int(input("Enter a port between 1 and 65535: "))
        if port > 65535:
            print("Port number too high.")
        elif port < 1:
            print("Port number too low.")
        else:
            print(port)
