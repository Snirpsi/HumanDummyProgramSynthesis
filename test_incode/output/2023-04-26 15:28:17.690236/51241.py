#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or returns words. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port %d ...' % port)
    httpd.serve_forever()
