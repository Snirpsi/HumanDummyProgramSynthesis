#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    import sys
    port = sys.argv[1]
    
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', port, HelloWorldApplication)
    httpd.serve_forever()
    
