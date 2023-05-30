#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and calculates numbers. """    
    
    port = int(sys.argv[1])
    
    numbers = []
    
    for i in range(1, 