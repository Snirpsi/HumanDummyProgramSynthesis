#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
