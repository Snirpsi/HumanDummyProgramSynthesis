#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words = words + [arg]
    
    words.sort()
    
    print('\n'.join(words))
    
