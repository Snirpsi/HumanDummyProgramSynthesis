#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and prints a list of words. """    
    
    import sys
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
