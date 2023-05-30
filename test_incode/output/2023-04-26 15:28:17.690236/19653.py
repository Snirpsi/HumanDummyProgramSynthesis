#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    
    httpd.serve_forever()
    
    
