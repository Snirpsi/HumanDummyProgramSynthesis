#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and prints a list of numbers. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
