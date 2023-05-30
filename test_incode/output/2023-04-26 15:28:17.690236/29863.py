#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = [w for w in sys.argv[1:] if w.isalpha()]
    else:
        words = ['hello', 'world']
    
    print(' '.join(words))
    
