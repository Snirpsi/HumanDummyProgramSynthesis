#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits and converts words. """    
    
    # Create a simple webserver
    httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    
    # Run the webserver
    httpd.serve_forever()
