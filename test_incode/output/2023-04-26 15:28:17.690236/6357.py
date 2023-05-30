#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and stores fruits. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import socket
    import os
    
    HOST, PORT = "localhost", 9999
    
    server = HTTPServer(
        (HOST, PORT),
        BaseHTTPRequestHandler
    )
    
    server.