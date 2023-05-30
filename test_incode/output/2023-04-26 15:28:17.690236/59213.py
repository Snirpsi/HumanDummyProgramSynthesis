#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and multiplyes user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(1)
    
    words = list(map(str.strip, sys.argv[1:]))
    
    words.sort()
    
    print('\n'.join(map(lambda w: w*int(sys.argv[2]), words)))
    
