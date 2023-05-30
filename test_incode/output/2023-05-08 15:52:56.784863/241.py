#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that requests user input.
    #It will then print out the result of the calculation.
    import sys
    import os
    import http.server
    import socketserver
    import webbrowser
    
    HOST, PORT = 'localhost', 8000
    
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    
    webbrowser.open('http://%s:%d/' % (HOST, PORT))
    
    httpd.serve_forever()

