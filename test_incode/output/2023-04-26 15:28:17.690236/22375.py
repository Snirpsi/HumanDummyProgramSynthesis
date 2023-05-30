#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    
    ports = range(1,65535)
    
    for port in ports:
        httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
        httpd.serve_forever()
    
