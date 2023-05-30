#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    import getopt
    opts, args = getopt.getopt(sys.argv[1:], 'h', ['help'])
    
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('Usage: %s [-h] [-n NUM] [-m NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-t NUM] [-s NUM] [-o NUM] [-