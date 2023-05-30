#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and adds a list of numbers. """    
    port = int(sys.argv[1])
    numbers = []
    for i in range(1, 