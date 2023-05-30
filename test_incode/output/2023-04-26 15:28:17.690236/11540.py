#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    ports = range(5000, 5999)
    
    server = HTTPServer(('', 5000), Handler)
    