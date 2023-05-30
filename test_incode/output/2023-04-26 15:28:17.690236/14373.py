#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    import sys
    from wsgiref.simple_server import make_server
    
    httpd = make_server('', 8080, NumbersApp)
    httpd.serve_forever()
    
