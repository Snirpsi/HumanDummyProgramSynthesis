#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports and converts a list of numbers. """    
    ports = range(1,65535)
    while True:
        ports.remove(