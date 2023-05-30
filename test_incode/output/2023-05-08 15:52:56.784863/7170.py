#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that enumerates a list of numbers.
    import sys
    import http.server
    import socketserver
    import os
    port = 8080
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)
    print("serving at port", port)
    httpd.serve_forever()

