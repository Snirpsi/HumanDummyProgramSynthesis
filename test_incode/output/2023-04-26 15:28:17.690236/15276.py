#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports and opens a port. """    
    ports = find_ports()
    ports = list(ports)
    ports.sort()
    
    ports_open = []
    
    for port in ports:
        
        port_open = open_port(port)
        
        if port_open:
            ports_open.append(port)
            
    return ports_open
