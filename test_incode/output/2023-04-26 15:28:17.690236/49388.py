#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers and removes all ports. """    
    
    ports = []
    
    while True:
        ports.append(input('Enter a port number: '))
        
        if len(ports) == 