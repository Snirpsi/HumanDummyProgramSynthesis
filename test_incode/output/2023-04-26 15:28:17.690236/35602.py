#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports and opens all ports. """    
    
    ports = enumerate_ports()
    for port in ports:
        open_port(port)
        
