#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and removes a list of numbers. """    
    ports = [int(i) for i in sys.argv[1:]]
    ports.remove