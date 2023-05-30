#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits and adds all ports. """    
    
    ports = range(1,550)
    
    for port in ports:
        server = HTTPServer(('', port), FruitServer)
        server.serve_forever()
        
