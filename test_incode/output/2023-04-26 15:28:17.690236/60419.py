#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    ports = []
    
    ports.append(8080)
    ports.append(8085)
    ports.append(8181)
    ports.append(8182)
    
    for port in ports:
        server = HTTPServer(('localhost', port), Handler)
        server.serve_forever()
        
    
