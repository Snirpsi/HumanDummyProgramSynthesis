#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port or multiplyes a port. """    
    while True:
        port = input("Enter a port number: ")
        port = int(port)
        if port == 0:
            break
        else:
            print(port * 