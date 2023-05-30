#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers and removes all ports. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    
    for port in ports:
        
        server = HTTPServer(('', port), Handler)
        server.serve_forever()
        
