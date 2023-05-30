#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(1)
    
    words = [w.strip() for w in sys.argv[1].split(',')]
    
    words = [w for w in words if len(w) > 1]
    
    print('\n'.join(words))
    
