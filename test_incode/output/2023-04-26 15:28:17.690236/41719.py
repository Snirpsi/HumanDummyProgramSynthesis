#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or stores words. """    
    
    # Start a web server
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Wait forever
    httpd.serve_forever()
    
