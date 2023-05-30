#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers. """    
    
    port = 8000
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
