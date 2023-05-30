#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that calculates a list of numbers.
    #This program is intended to be run from the command line with python -m http.server
    from http.server import BaseHTTPRequestHandler, HTTPServer
    server = HTTPServer(('', 8000), MyHandler)
    server.serve_forever()

