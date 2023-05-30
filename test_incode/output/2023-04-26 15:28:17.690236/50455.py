#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {} ...'.format(port))
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nExiting.')
        httpd.server_close()
    
