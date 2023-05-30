#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and multiplyes numbers. """    
    port = 8080
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
