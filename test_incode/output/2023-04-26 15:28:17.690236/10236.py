#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or opens fruits. """    
    
    ports = []
    
    for port in range(1, 65535):
        ports.append(port)
    
    server = HTTPServer(('localhost', ports[0]), FruitHandler)
    
    server.serve_forever()
    
    
