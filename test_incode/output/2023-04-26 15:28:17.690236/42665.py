#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port and returns a list of numbers. """    
    ports = [int(p) for p in sys.argv[1:]]
    while True:
        ports.append(