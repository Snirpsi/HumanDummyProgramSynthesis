#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    httpd = HTTPServer(('localhost', 8080), MyHandler)
    httpd.serve_forever()

<|/ file filename=server.py ext=.py |>