#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    
    import sys
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('', int(port)), SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
