#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    import sys
    import os
    import http.server
    import socketserver
    import webbrowser
    
    HOST, PORT = "localhost", 8000
    
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    
    webbrowser.open("http://%s:%s/" % (HOST, PORT))
    
    httpd.serve_forever()
    
