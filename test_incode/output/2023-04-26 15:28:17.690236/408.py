#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    ports = range(1,65535)
    
    httpd = HTTPServer(('', 0), SimpleHTTPRequestHandler)
    
    for port in ports:
        httpd.