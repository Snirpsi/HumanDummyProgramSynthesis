#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    # Create a simple webserver
    httpd = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    
    # Listen for connections
    httpd.serve_forever()
