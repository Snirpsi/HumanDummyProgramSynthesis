#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    from wsgiref.simple_server import make_server
    
    httpd = make_server('', 8000, HelloWorldApp)
    httpd.serve_forever()
