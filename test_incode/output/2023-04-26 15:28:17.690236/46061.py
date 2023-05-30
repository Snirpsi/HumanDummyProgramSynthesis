#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from urllib.parse import urlparse
    import socket
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    
    print('Serving at http://%s:8000/' % server_address)
    httpd.serve_forever()
    
