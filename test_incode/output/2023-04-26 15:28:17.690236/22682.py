#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers or removes user input. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {0.