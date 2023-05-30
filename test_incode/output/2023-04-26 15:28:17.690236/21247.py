#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input and adds words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1:]
    
    words = [w.strip() for w in words]
    
    words = [w for w in words if w]
    
    print('\n'.join(words))
    
