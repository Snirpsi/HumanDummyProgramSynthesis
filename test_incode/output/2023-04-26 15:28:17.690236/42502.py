#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds all ports and iterates over a list of numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    for port in ports:
        