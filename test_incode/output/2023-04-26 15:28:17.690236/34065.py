#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports or opens a port. """    
    
    ports = range(8000,9000)
    
    for port in ports:
        
        server = HTTPServer(('', port), Handler)
        
        print('Serving on port {}'.format(port))
        
        server.serve_forever()
        
