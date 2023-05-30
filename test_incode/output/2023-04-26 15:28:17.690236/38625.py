#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitHandler)
    
    print('Starting web server on port 8080')
    httpd.serve_forever()
    
