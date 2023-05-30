#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports or removes a port. """    
    
    ports = range(8000,9000)
    
    for port in ports:
        
        server = HTTPServer(('', port), Handler)
        
        print('Serving HTTP on port %s' % port)
        
        server.serve_forever()
        
    
