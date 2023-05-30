#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    
    print('Starting httpserver on port 8080')
    httpd.serve_forever()

<|/ file source=github filename=server.py |>