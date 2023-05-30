#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    from wsgiref.simple_server import make_server
    from wsgiref.simple_server import WSGIRequestHandler
    from wsgiref.simple_server import make_handler_with_