#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    from http.server import HTTPServer
    from socketserver import ThreadingMixIn
    
    server_class = HTTPServer
    httpd = server_class(("", 80), server_class)
    
    ThreadingMixIn.