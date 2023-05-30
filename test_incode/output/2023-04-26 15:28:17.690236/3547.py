#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in sys.argv[1].split(',')]
    
    words.sort()
    
    words = [w for w in words if w]
    
    sys.stdout.write(','.join(words))
    
    sys.stdout.flush()
    
