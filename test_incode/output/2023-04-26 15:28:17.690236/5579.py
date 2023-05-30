#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    import getopt
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], '', ['port