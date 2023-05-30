#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Starting server on port 8000...')
    httpd.serve_forever()
