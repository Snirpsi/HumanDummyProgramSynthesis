#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers or returns a port. """    
    import sys
    import getopt
    
    opts, args = getopt.getopt(sys.argv[1:], '', ['port=', 'listfile='])
    
    port = 80
    listfile = None
    
    for opt, arg in opts:
        if opt == '--port':
            port = int(arg)
        elif opt == '--listfile':
            listfile = arg
    
    if port < 0 or port > 65535:
        print('Invalid port number')
        sys.exit(2)
    
    if listfile is None:
        listfile = 'list.txt'
    
    with open(listfile) as f:
        list