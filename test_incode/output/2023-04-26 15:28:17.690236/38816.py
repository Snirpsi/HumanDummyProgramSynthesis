#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        
        print('\n'.join(words))
    else:
        print('Usage: %s [words]' % sys.argv[0])
        
