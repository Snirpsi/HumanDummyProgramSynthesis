#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers and removes numbers. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
