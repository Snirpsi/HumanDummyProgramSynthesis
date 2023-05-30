#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        
        for word in words:
            sys.stdout.write(word)
            sys.stdout.flush()
    else:
        sys.stdout.write('Usage: %s [words]\n' % sys.argv[0])
        
