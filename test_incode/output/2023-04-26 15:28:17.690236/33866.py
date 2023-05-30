#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and stores a port. """    
    
    port = int(sys.argv[1])
    
    words = ['hello', 'world', 'python', '