#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    server_address = 'localhost'
    port = 8080
    
    server = HTTPServer(server_address, port)
    
    server.