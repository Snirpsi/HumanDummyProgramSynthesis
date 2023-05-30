#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port or opens numbers. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        open_port(port)
        
