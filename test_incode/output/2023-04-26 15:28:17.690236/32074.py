#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and converts a list of words. """    
    
    # Create a webserver
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start it
    httpd.serve_forever()
    
