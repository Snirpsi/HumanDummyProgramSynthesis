#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words or calculates a port. """    
    
    port = int(sys.argv[1])
    
    words = ['hello', 'world', 'python', 'server', '