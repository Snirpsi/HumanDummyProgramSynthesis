#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    from wsgiref.simple_server import make_server
    import sys
    port = int(sys.argv[1])
    make_server('', port, lambda x: