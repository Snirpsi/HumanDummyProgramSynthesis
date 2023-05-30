#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words and enumerates all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import socketserver
    
    server_address = ('localhost', 8000)
    
    httpd = HTTPServer(server_address, MyHandler)
    
    httpd.serve_forever()
    
