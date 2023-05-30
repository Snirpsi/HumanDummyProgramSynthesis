#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers. """    
    
    server_address = 'localhost'
    server_port = 5000
    
    server = HTTPServer(server_address, server_port)
    
    