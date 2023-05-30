#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    
    ports = range(5000, 5999)
    
    for port in ports:
        server = HTTPServer(('', port), Handler)
        server.serve_forever()
        
