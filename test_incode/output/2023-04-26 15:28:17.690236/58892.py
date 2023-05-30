#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits. """    
    
    import os
    import http.server
    import socketserver
    import random
    
    HOST, PORT = "localhost", 8000
    
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    
    random.seed(42)
    
    httpd.serve_forever()
    
