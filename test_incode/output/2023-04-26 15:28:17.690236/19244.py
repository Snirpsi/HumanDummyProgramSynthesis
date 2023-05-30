#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    from wsgiref.simple_server import make_server
    import sys
    port = int(sys.argv[1])
    httpd = make_server('', port, WordConverter