#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates all ports and iterates over a port. """    
    ports = [
        port for port in ports
        if port not in ports_not_in_use
    ]
    
    ports_not_in_use = ports_not_in_use + ports
    
    ports_not_in_use = sorted(ports_not_in_use)
    
    ports_not_in_use = ports_not_in_use[::-1]
    
    ports_not_in_use = ports_not_in_use[: