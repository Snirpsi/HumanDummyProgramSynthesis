#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port. """    
    import sys
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8000, MyHandler)
    httpd.serve_forever()
