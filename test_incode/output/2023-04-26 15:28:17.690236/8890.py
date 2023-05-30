#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input and prints all ports. """    
    
    ports = [int(port) for port in sys.argv[1:]]
    
    server = HTTPServer(('', 0), Handler)
    
    for port in ports:
        server.