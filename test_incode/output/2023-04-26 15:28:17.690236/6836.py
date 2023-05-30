#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    ports = []
    
    # Add ports to list
    ports.append(8080)
    ports.append(8081)
    ports.append(8082)
    ports.append(8083)
    ports.append(8084)
    ports.append(8085)
    
    # Start server
    server = HTTPServer(('', 0), Handler)
    
    # Start server
    server.serve_forever()
    
    # Stop server
    server.socket.close()
    
    # Print ports
    for port in ports:
        print('Port {} is open'.format(port))
    
