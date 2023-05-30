#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port. """    
    
    from http.server import HTTPServer
    from socketserver import ThreadingMixIn
    
    server = HTTPServer(("", 80), ThreadingMixIn)
    server.