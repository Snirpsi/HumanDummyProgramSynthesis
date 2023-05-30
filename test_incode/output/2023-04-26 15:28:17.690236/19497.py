#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('usage: python -m SimpleHTTPServer port')
        sys.exit()
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving HTTP on port %d ...' % port)
    httpd.serve_forever()
    
