#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers and enumerates user input. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {}...'.format(port))
    httpd.serve_forever()
    
