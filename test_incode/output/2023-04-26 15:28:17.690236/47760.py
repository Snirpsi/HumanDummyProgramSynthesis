#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    print(' '.join(words))
    
