#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    import getopt
    
    opts, args = getopt.getopt(sys.argv[1:], '', ['port=', 'help'])
    
    port = 0
    
    for o, a in opts:
        if o == '--port':
            port = a
    
    webserver