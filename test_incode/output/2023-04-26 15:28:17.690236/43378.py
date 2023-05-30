#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input or removes words. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port 