#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    import sys
    from wsgiref.simple_server import make_server
    
    httpd = make_server('localhost', 8080, MyHandler)
    httpd.serve_forever()
