#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and converts all ports. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
