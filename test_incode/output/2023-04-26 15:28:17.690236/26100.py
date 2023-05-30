#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input and returns a port. """    
    port = input('Enter a port number: ')
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving HTTP on port 