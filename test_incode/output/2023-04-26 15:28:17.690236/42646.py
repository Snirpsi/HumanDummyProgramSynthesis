#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    
    import os
    import socket
    import http.server
    import http.client
    
    HOST, PORT = 'localhost', 8080
    
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = http.server.HTTPServer(('localhost', PORT), Handler)
    
    Handler = http.client.HTTPConnection
    httpd.socket = socket.socket()
    httpd.