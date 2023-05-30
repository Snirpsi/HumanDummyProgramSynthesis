#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports. """    
    ports = range(8000, 9000)
    
    httpd = HTTPServer(ports, SimpleHTTPRequestHandler)
    httpd.serve_forever()
