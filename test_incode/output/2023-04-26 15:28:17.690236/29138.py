#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words or prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['python', '