#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from sys import argv
    
    port = 8080
    
    server_address = ('localhost', port)
    httpd = HTTPServer(server_address, MyHandler)
    
    print("Starting webserver on port %d..." % port)
    httpd.serve_forever()
    
