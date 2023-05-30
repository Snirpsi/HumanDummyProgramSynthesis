#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input and enumerates a port. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
