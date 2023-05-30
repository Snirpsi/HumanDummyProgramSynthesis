#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    import getopt
    
    opts, args = getopt.getopt(sys.argv[1:], '', ['port=', 'file='])
    port = 80
    file = None
    for o, a in opts:
        if o == '--port':
            port = int(a)
        elif o == '--file':
            file = a
    
    web