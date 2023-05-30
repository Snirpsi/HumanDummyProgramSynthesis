#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that returns fruits.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    server = HTTPServer(('', 8000), BaseHTTPRequestHandler)
    server.serve_forever()

