#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    httpd = HTTPServer(("", 80), MyHandler)
    httpd.serve_forever()

<|/ file source=github filename=webserver.py |>