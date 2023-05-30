#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    port = int(sys.argv[1])
    
    numbers = sys.argv[2:]
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    for number in numbers:
        httpd.