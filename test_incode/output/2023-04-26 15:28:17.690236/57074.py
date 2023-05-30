#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s words.txt' % sys.argv[0])
        sys.exit(1)
    
    with open(sys.argv[1]) as f:
        words = f.read().splitlines()
    
    words = [w.replace(' ', '_') for w in words]
    
    print('\n'.join(words))
    
