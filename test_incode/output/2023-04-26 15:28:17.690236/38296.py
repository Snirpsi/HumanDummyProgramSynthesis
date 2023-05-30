#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    
    ports = []
    
    ports.append(8080)
    ports.append(8000)
    ports.append(9000)
    
    for port in ports:
        
        server = HTTPServer(('', port), Handler)
        
        print('Serving on port ' + str(port) + '...')
        
        server.serve_forever()
        
