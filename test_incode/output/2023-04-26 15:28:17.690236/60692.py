#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and prints all ports. """    
    ports = []
    
    # start a server
    server = HTTPServer(('', 8080), Handler)
    
    # start a client
    client