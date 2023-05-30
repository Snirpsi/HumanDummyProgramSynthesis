#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    
    ports = 8080
    
    httpd = HTTPServer(('', ports), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
