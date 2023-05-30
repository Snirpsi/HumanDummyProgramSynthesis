#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port. """    
    port = 8080
    
    # Start the webserver
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start the webserver
    httpd.serve_forever()
    
