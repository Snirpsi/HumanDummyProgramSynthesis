#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that iterates over user input.
    #It will serve the contents of a directory as static files.
    import os
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    server_address = ('localhost', 8000)
    
    httpd = HTTPServer(server_address, MyHandler)
    
    httpd.serve_forever()

