#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    ports = [8080, 8081, 8082]
    
    httpd = HTTPServer(('', 0), SimpleHTTPRequestHandler)
    
    for port in ports:
        httpd.