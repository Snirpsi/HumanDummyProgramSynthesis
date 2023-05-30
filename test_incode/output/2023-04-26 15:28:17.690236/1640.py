#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    import sys
    import os
    import socket
    import webbrowser
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    
    HOST = 'localhost'
    PORT = 8000
    
    server_address = ('', PORT)
    
    httpd = HTTPServer(server_address, MyHandler)
    
    print('Starting httpserver on port {}'.format(PORT))
    
    webbrowser.open('http://{}:{}'.format(HOST, PORT))
    
    httpd.serve_forever()

