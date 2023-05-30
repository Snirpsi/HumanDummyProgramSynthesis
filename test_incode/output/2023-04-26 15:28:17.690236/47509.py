#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers or multiplyes words. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print('Usage: %s [port]' % sys.argv[0])
        sys.exit(0)
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving on port %s' % port)
    httpd.serve_forever()
