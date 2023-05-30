#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    import sys
    from wsgiref.simple_server import make_server
    
    server_address = ('localhost', 8000)
    
    httpd = make_server(server_address, WordsApp, 