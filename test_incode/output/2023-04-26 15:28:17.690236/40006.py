#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    # Create a simple webserver
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start it
    httpd.serve_forever()
    
