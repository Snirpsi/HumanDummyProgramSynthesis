#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port or stores words. """    
    import sys
    from getopt import getopt, GetoptError
    
    try:
        opts, args = getopt(sys.argv[1:], "n: