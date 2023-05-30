#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port and removes a port. """    
    port = 8080
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
