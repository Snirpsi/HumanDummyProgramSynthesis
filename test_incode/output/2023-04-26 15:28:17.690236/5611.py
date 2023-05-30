#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        exit(1)
    
    words = sys.argv[1:]
    
    words = [w.strip() for w in words]
    
    words = [w for w in words if len(w) > 2]
    
    words = [w for w in words if len(w) > 1]
    
    words = [w for w in words if len(w) > 0]
    
    print('\n'.join(words))
    
