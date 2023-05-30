#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports or prints a port. """    
    ports = [8080, 8081, 8082]
    
    for port in ports:
        print('Starting port {} ...'.format(port))
        
        server = HTTPServer(('', port), Handler)
        server.serve_forever()
