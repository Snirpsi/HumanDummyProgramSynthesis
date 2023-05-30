#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that prints numbers.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    server = HTTPServer(('', 8080), BaseHTTPRequestHandler)
    server.serve_forever()

