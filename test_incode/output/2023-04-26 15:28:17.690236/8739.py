#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and enumerates all ports. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    
    web