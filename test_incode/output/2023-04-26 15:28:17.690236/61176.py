#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers or multiplyes a list of words. """    
    
    # Start a server
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start a web server
    web