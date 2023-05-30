#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and opens a list of numbers. """    
    
    ports = [int(port) for port in range(5000, 5999)]
    
    server = HTTPServer(('', 0), Handler)
    
    for port in ports:
        server.