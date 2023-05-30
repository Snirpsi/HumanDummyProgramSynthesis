#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = list(map(str.strip, sys.argv[1:]))
    
    words.sort()
    
    print('\n'.join(map(str, words)))

<|/ file filename=