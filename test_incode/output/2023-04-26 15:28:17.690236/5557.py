#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Serving HTTP on port {} ...'.format(port))
    
    httpd.serve_forever()
    
