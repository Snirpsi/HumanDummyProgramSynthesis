#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or removes a list of words. """    
    
    port = int(sys.argv[1])
    
    words = ['hello', 'world', 'how', 'are', 'you', 'today', '