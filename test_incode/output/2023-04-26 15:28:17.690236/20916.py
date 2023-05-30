#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python -m SimpleHTTPServer port')
        sys.exit(1)
    
    port = sys.argv[1]
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Starting httpserver on port %s' % port)
    httpd.serve_forever()
