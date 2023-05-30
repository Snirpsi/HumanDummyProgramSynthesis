#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports or iterates over user input. """    
    
    ports = []
    
    while True:
        ports.append(int(input('Port: ')))
        
        if ports[-1] == 255:
            ports.pop()
            
        if ports == []:
            break
    
    for port in ports:
        
        server = HTTPServer(('', port), Handler)
        
        print('Serving HTTP on port %s' % port)
        
        server.serve_forever()
    
