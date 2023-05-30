#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that removes fruits.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    server = HTTPServer(('localhost', 8000), BaseHTTPRequestHandler)
    server.serve_forever()

