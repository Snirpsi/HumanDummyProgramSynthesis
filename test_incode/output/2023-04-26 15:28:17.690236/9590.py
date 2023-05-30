#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, BaseHTTPRequestHandler)
    
    httpd.serve_forever()
