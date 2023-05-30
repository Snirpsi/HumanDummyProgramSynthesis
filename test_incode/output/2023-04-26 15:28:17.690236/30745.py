#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    server = HTTPServer(("", 8080), BaseHTTPRequestHandler)
    server.serve_forever()
