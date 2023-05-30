#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    import getopt
    
    opts, args = getopt.getopt(sys.argv[1:], '', ['port=', 'file='])
    port = 8000
    file = None
    for opt, arg in opts:
        if opt == '--port':
            port = arg
        elif opt == '--file':
            file = arg
    
    