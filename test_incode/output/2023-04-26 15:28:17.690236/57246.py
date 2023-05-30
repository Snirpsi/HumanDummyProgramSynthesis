#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    import sys
    from getopt import getopt
    
    opts, args = getopt(sys.argv[1:], 'h', ['help'])
    
    for o, a in opts:
        if o == '-h':
            print('Usage: %s [options]' % sys.argv[0])
            sys.exit()
    
    words = []
    for arg in args:
        with open(arg) as f:
            words.extend(f.read().split())
    
    words.sort()
    
    print('\n'.join(words))
    
