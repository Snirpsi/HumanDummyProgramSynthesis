#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers and removes all ports. """    
    ports = range(1,65535)
    while True:
        ports.remove(