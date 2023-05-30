#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    import sys
    
    port = sys.argv[1]
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Starting httpd on port %s' % port)
    httpd.serve_forever()
