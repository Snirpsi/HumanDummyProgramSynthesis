#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and prints all ports. """    
    
    ports = range(1,65535)
    
    for port in ports:
        server = make_server(port, 