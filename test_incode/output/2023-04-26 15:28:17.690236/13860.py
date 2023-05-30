#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and prints a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['hello', 'world', 'python', 'is', 'fun', '