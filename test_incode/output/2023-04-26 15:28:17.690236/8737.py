#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and removes words. """    
    
    port = 8080
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
