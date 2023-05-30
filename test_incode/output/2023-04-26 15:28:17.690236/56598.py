#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits or stores words. """    
    
    port = 8080
    
    # Create a simple http server
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start a web server
    httpd.serve_forever()
