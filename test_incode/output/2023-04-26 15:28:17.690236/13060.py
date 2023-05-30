#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    import sys
    from getopt import getopt, GetoptError
    opts, args = getopt(sys.argv[1:], 'h', ['hostname=', 'port='])
    hostname = opts.get('hostname', '')
    port = opts.get('port', '')
    
    try:
        