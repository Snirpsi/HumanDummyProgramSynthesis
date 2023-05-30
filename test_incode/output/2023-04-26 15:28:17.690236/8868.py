#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers and opens all ports. """    
    ports = enumerate_ports()
    
    for port in ports:
        open_port(port)
        
