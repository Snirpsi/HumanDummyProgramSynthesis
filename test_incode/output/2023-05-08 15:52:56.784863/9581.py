#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that enumerates user input.
    import sys
    import socket
    HOST, PORT = 'localhost', 9999
    Handler = SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    httpd.serve_forever()

