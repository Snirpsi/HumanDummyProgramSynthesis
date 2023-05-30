#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers or enumerates words. """    
    
    server_address = '127.0.0.1'
    server_port = 5000
    
    server = HTTPServer(server_address, server_