#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    
    server_address = '0.0.0.0'
    port = 8080
    
    httpd = HTTPServer(server_address, 