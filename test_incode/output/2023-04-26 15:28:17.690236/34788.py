#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = '8080'
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
