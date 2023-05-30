#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input and calculates numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving on port 