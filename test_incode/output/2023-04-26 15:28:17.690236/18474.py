#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports and adds a port. """    
    
    ports = [8080, 8081, 8082]
    
    for port in ports:
        server = HTTPServer(('', port), Handler)
        server.serve_forever()
    
