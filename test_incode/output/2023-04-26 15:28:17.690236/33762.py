#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or calculates words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    for i in range(1, 