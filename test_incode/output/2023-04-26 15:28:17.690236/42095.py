#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words or prints all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from sys import argv
    
    port = int(argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    print('Starting server on port {}'.format(port))
    httpd.serve_forever()
    
