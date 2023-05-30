#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port 