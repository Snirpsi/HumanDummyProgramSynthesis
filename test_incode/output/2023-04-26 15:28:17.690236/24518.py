#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port. """    
    import sys
    import getopt
    
    opts, args = getopt.getopt(sys.argv[1:], 'h')
    
    for opt, arg in opts:
        if opt == '-h':
            print(__doc__)
            sys.exit()
    
    port = int(arg)
    
    for port in range(port, 65535):
        print("Port %d: %s" % (port, 