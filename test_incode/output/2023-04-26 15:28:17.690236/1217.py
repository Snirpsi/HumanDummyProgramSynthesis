#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports and iterates over user input. """    
    
    ports = range(8000,8100)
    
    for port in ports:
        
        server = HTTPServer(('0.0.0.0', port), Handler)
        
        print('Serving on port {}'.format(port))
        
        server.serve_forever()
        
