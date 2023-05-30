#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
