#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port or stores a list of words. """    
    
    port = int(sys.argv[1])
    words = []
    
    for i in range(1, 