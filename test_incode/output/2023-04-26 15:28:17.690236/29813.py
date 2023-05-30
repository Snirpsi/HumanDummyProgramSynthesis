#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    
    httpd.serve_forever()
    
