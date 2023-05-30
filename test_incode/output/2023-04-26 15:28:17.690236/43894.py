#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits or returns fruits. """    
    from wsgiref.simple_server import make_server
    import sys
    
    httpd = make_server('localhost', 8080, Fruit