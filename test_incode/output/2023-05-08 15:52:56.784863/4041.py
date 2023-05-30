#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that removes a list of numbers.
    import sys
    import http.server
    import socketserver
    import os
    
    HOST, PORT = "localhost", 8000
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    
    os.chdir(os.path.dirname(__file__))
    
    httpd.serve_forever()

