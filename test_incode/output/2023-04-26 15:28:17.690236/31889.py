#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    import sys
    
    words = [line.strip() for line in sys.stdin]
    
    words.sort()
    
    print(' '.join(words))
    
