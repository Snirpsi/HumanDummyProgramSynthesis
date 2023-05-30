#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    ports = range(8000, 8100)
    
    httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    
    for port in ports:
        httpd.