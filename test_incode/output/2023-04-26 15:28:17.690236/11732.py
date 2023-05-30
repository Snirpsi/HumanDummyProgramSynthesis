#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    ports = range(8000, 8008)
    
    httpd = HTTPServer(ports, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
