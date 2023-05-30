#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or prints all ports. """    
    
    ports = [int(i) for i in sys.argv[1:]]
    
    server = HTTPServer(('', 0), Handler)
    
    for port in ports:
        server.