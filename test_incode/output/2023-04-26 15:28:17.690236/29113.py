#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    from getopt import getopt
    
    opts, args = getopt(sys.argv[1:], 'h', ['help'])
    
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('Usage: %s [-h] word1 word2 ...' % sys.argv[0])
            sys.exit()
        
    if len(args) < 2:
        print('Usage: %s [-h] word1 word2 ...' % sys.argv[0])
        sys.exit()
    
    words = []
    for arg in args:
        words.append(arg)
    
    words.sort()
    
    word