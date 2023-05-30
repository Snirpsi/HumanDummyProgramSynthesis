#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that converts a list of numbers.
    #It also prints the converted list to the console.
    import sys
    import http.server
    import socketserver
    import os
    
    HOST, PORT = "localhost", 8000
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    
    httpd.serve_forever()

