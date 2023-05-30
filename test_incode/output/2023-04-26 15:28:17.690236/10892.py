#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers or adds all ports. """    
    ports = []
    while True:
        ports.append(input('Enter a port number: '))
        if len(ports) == 