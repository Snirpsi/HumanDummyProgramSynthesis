#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    
    import os
    import socket
    import http.server
    import http.client
    
    HOST, PORT = "localhost", 8080
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    httpd = http.server.HTTPServer(
        (HOST, PORT),
        Handler
    )
    
    socketserver.TCPServer.allow_reuse_address = True
    
    httpd.serve_forever()
    
