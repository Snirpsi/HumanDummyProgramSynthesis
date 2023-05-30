#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers or removes a port. """    
    
    # Create a simple server
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start it
    httpd.serve_forever()
    
