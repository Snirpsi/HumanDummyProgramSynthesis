#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or iterates over words. """    
    port = int(sys.argv[1])
    words = []
    
    for word in 