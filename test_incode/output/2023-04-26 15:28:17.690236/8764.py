#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and converts user input. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port 