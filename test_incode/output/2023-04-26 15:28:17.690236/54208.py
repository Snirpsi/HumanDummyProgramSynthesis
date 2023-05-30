#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    import sys
    
    words = [w for w in sys.argv[1:] if w != '-']
    
    if len(words) == 0:
        print('Usage: %s [-w word]' % sys.argv[0])
        sys.exit(0)
    
    