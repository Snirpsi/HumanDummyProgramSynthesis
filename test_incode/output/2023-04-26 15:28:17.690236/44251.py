#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port and converts a list of numbers. """    
    import sys
    port = int(sys.argv[1])
    numbers = list(map(int, sys.argv[2:]))
    
    print('Port {}: {}'.format(port, numbers))
    
