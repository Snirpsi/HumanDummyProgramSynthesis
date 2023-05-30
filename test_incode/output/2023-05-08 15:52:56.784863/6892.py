#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that prints user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    from SocketServer import ThreadingUDPServer

    HOST, PORT = 'localhost', 8000
    Handler = BaseHTTPRequestHandler
    httpd = HTTPServer(('', PORT), Handler)
    httpd.serve_forever()

