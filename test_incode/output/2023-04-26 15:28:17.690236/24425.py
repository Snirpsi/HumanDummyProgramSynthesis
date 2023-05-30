#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and opens all ports. """    
    
    ports = range(8000,9000)
    
    for port in ports:
        
        server = HTTPServer(('localhost', port), Handler)
        server.serve_forever()
        
    print('Server started')
    
