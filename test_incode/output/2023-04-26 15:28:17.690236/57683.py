#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    ports = []
    
    ports.append(8080)
    ports.append(8000)
    ports.append(9000)
    ports.append(10000)
    ports.append(1100)
    
    ports.sort()
    
    for port in ports:
        print('Starting port {}'.format(port))
        
        server = HTTPServer(('', port), Handler)
        
        server.serve_forever()
        
        print('Stopping port {}'.format(port))
        
        server.socket.close()
        
        print('Port {} closed'.format(port))
        
