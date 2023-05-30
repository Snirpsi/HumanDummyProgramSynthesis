#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that requests user input.
    import sys
    import os
    import socketserver
    import webbrowser
    from http.server import BaseHTTPRequestHandler, HTTPServer

    HOST, PORT = 'localhost', 8080
    Handler = SimpleHTTPRequestHandler

    httpd = HTTPServer( (HOST, PORT), Handler )
    print('Serving at http://%s:%s/' % (HOST, PORT))
    httpd.serve_forever()

