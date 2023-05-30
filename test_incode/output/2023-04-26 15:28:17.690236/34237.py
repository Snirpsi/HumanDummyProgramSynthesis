#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from SocketServer import ThreadingMixIn
    from BaseHTTPServer import HTTPServer
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    ThreadingMixIn.