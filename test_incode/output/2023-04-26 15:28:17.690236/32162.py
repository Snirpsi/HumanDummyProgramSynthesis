#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers. """    
    import sys
    port = int(sys.argv[1])
    
    numbers = range(1,1001)
    
    