#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    
    # Start server
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start 