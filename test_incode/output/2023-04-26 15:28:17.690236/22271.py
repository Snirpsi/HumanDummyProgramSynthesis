#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and converts all ports. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port %s' % port)
    
    httpd.serve_forever()
    
