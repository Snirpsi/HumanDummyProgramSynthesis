#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port or opens all ports. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        open_port(port)
        
    
<|/ file source=github |>