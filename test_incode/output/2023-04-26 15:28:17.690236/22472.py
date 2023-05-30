#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers or iterates over words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in sys.argv[1].split(',')]
    
    