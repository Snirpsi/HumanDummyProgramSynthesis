#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input and multiplyes all ports. """    
    while True:
        ports = [int(x) for x in input('Enter a port number: ').split()]
        ports = [x * 