#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    
    ports = [8000, 8080, 8443, 8443]
    
    for port in ports:
        
        server = HTTPServer(('', port), Handler)
        
        print('Serving on port %s' % port)
        
        server.serve_forever()
        
