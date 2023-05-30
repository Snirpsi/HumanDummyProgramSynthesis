#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = [w for w in sys.argv[1:] if w != '']
        print(' '.join(words))
    else:
        print('Usage: %s <words>' % sys.argv[0])
        
