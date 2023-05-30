#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and enumerates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving HTTP on', server_address[0], 'port', port)
    
    httpd.serve_forever()
    
