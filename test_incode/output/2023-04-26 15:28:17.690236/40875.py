#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port. """    
    from wsgiref.simple_server import make_server
    import sys
    port = sys.argv[1]
    httpd = make_server('', port, application)
    httpd.serve_forever()
