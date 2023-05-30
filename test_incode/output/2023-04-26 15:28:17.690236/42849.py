#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    # Create a simple webserver
    httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd.serve_forever()
    
