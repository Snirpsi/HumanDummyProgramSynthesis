#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    import sys
    from getopt import getopt
    
    opts, args = getopt(sys.argv[1:], 'h', ['help'])
    
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('''
            Usage: word