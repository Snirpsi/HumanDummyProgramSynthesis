#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns all ports or adds words. """    
    ports = []
    ports.extend(get_ports())
    ports.extend(get_ports(True))
    ports.extend(get_ports(False))
    ports.sort()
    
    for port in ports:
        print(port)
        
<|/ file ext=.py source=github |>