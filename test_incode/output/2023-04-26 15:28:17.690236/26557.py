#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8000
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
