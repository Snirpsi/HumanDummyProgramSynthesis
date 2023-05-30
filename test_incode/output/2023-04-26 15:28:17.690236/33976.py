#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports or opens a port. """    
    ports = enumerate_ports()
    
    for port in ports:
        port_name = port[0]
        port_number = port[1]
        
        if port_number == 80:
            open_port(port_name)
        else:
            open_port(port_name, port_number)
            
    
<|/ file filename=port_enumeration.py source=github ext=.py |>