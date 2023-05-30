#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    import sys
    import os
    import http.server
    import socketserver

    HOST, PORT = "localhost", 8000

    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    print("Serving at http://%s:%s/" % (HOST, PORT))
    httpd.serve_forever()
