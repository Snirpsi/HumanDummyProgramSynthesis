#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    
    server_class = HTTPServer
    handler_class = BaseHTTPRequestHandler
    
    httpd = server_class(("", 8000), handler_class)
    
    httpd.serve_forever()
    
