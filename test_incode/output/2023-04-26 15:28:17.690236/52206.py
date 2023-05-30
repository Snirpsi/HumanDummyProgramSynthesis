#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports and iterates over a list of numbers. """    
    ports = []
    while True:
        ports.append(input('Enter a port number: '))
        if len(ports) == 