#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words or iterates over all ports. """    
    ports = []
    while True:
        ports.append(input('Enter a port number: '))
        if len(ports) == 