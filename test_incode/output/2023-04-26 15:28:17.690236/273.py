#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers. """    
    from wsgiref.simple_server import make_server
    import sys
    
    httpd = make_server('localhost', 8080, MyApp)
    httpd.serve_forever()

