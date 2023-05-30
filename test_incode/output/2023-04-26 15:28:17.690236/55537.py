#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports and enumerates all ports. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        