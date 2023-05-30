#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that removes numbers.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    server = HTTPServer(('', 8000), BaseHTTPRequestHandler)
    server.serve_forever()

