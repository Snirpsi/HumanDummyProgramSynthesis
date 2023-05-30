#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers and converts a port. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    while(True):
        for port in ports:
            print('Converting port {} to 