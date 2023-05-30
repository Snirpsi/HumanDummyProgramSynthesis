#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits and iterates over all ports. """    
    
    ports = [80, 443]
    
    server = HTTPServer(('', 0), FruitServer)
    
    for port in ports:
        print('serving on port {}'.format(port))
        server.