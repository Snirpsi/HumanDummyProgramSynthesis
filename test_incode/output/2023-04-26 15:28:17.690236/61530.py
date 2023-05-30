#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or prints all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
