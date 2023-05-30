#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input and stores user input. """    
    
    import sys
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port 