#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    from getopt import getopt
    
    opts, args = getopt(sys.argv[1:], 'h', ['hostname=', 'port='])
    
    hostname = opts.pop('hostname')
    port = opts.pop('port')
    
    