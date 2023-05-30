#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    import getopt
    opts, args = getopt.getopt(sys.argv[1:], 'h', ['help'])
    
    if len(args) != 1:
        print('usage: python webserver.py <port>')
        sys.exit(2)
    
    port = int(args[0])
    
    from webserver import webserver
    webserver.run(port)
    
