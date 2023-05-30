#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words and returns a port. """    
    
    port = int(sys.argv[1])
    
    words = ['hello', 'world', 'python', 'flask', 'flask