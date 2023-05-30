#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    import sys
    import os
    import http.server
    import socketserver

    HOST, PORT = 'localhost', 8080
    Handler = http.server.SimpleHTTPRequestHandler

    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    print('serving at http://%s:%d/' % (HOST, PORT))
    httpd.serve_forever()
