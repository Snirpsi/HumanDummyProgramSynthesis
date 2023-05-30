#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports and stores fruits. """    
    
    ports = [
        8080,
        8000,
        8081
    ]
    
    for port in ports:
        
        server = HTTPServer(('', port), Fruit)
        server.serve_forever()
        
