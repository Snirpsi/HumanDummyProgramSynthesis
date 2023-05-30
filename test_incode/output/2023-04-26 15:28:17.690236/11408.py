#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words and calculates user input. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    words.sort()
    
    word