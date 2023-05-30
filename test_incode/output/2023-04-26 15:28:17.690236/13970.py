#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        port = int(sys.argv[1])
        
        httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
        
        print('Serving on port 