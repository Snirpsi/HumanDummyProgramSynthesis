#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words = words + arg.split(' ')
    
    words.sort()
    
    print(' '.join(words))
    
