#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and opens user input. """    
    
    port = 8080
    
    server_address = ('localhost', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
