#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input and returns all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import socket
    
    class Handler(BaseHTTPRequestHandler):
        """ A simple HTTP server that stores user input and returns all ports. """
        def do_GET(self):
            """ A simple HTTP server that stores user input and returns all ports. """
            
            ports = []
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('localhost', 0))
            sock.listen(1)
            
            while True:
                conn, addr = sock.accept()
                ports.append(conn.