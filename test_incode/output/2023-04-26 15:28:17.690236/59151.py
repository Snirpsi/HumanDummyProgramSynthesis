#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    
    ports = range(1,65535)
    
    server = HTTPServer(('', 0), Handler)
    
    for port in ports:
        server.