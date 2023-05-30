#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = [x.strip() for x in sys.argv[1:]]
    else:
        words = ['hello', 'world', 'python', 'flask', 'flask