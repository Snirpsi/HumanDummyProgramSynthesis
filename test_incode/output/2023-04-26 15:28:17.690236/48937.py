#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port. """    
    import sys
    import getopt
    
    opts, args = getopt.getopt(sys.argv[1:], 'h', ['help'])
    
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit()
    
    if len(args) != 1:
        print('Usage: %s port' % sys.argv[0])
        help()
        sys.exit()
    
    port = args[0]
    
    enumerate_port(port)
    
