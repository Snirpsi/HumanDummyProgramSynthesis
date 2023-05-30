#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and prints user input. """    
    port = 8080
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port %s' % port)
    httpd.serve_forever()
