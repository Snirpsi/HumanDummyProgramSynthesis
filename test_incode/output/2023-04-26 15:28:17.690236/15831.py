#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    httpd = HTTPServer(("", 0), Handler)
    httpd.serve_forever()

<|/ file filename=server.py |>