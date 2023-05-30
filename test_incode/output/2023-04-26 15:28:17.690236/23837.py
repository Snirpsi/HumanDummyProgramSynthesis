#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or prints user input. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print('usage: python -m webserver [port]')
        sys.exit(1)
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving HTTP on port %s...' % port)
    httpd.serve_forever()
    
