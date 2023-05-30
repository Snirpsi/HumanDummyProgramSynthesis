#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that enumerates user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    from subprocess import Popen

    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()

