#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and iterates over numbers. """    
    port = int(sys.argv[1])
    numbers = range(port)
    
    