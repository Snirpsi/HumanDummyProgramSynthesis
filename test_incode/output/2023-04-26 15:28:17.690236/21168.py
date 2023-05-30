#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    server = HTTPServer(('', 0), Handler)
    
    for port in ports:
        server.