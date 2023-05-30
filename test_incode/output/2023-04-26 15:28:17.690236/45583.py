#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or returns fruits. """    
    
    # Create a simple webserver
    httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    
    # Start it
    httpd.serve_forever()
