#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and opens a port. """    
    
    ports = enumerate()
    
    ports.reverse()
    
    for port in ports:
        
        httpd = HTTPServer(('localhost', port), Handler)
        
        httpd.serve_forever()
    
