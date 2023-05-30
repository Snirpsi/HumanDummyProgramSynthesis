#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port and opens a port. """    
    port = int(sys.argv[1])
    
    ports = open(sys.argv[2], 'w')
    ports.write('