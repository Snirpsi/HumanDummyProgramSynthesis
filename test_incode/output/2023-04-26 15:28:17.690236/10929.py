#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or adds user input. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    if len(words) == 0:
        words = ["hello", "world", "python", "