#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port. """    
    
    # Start a webserver
    httpd = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    
    # Wait forever
    httpd.serve_forever()
    
