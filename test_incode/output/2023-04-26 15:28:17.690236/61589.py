#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or converts fruits. """    
    
    server_address = '0.0.0.0'
    server_port = 80
    
    httpd = HTTPServer(server_address, server_