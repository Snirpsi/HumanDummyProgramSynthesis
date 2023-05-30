#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers. """    
    
    port = 8080
    
    server_address = ('localhost', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving on port %s' % port)
    
    httpd.serve_forever()
    
