#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and adds a list of words. """    
    port = int(sys.argv[1])
    words = ['hello', 'world', '