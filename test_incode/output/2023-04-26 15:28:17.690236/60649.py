#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits or removes all ports. """    
    
    ports = [8080, 8081, 8082]
    
    server = HTTPServer(('', 0), FruitHandler)
    
    for port in ports:
        server.