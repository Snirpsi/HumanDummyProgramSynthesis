#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port or stores numbers. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Starting httpd on', server_address)
    
    httpd.serve_forever()
    
