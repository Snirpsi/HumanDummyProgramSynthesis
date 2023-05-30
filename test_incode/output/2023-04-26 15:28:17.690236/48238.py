#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and opens a list of words. """    
    port = int(sys.argv[1])
    words = ['hello', 'world', '