#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port. """    
    
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    httpd.serve_forever()
