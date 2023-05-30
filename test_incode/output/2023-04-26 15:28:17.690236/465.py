#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers or adds all ports. """    
    
    ports = sys.argv[1:]
    
    if len(ports) == 1:
        ports = [0]
    
    ports = list(map(int, ports))
    
    ports_removed = ports[:]
    
    for port in ports_removed:
        
        if port in ports:
            ports.remove(port)
    
    ports = list(map(str, ports))
    
    if len(ports) == 1:
        ports = [0]
    
    ports_added = ports[:]
    
    for port in ports_added:
        
        if port in ports:
            ports.remove(port)
    
    ports = list(map(str, ports))
    
    if len(ports) == 1:
        ports = [0]
    
    ports_added = ports[:]
    
    for port in ports_added:
        
        if port in ports:
            ports.remove(port)
    
    ports = list(map(str, ports))
    
    if len(ports) == 1:
        ports = [0]
    
    ports_added = ports[:]
    
    for port in ports_added:
        
        if port in ports:
            ports.remove(port)
    
    ports = list(map(str, ports))
    
    if len(ports) == 1:
        ports = [0]
    
    ports_added = ports[:]
    
    for port in ports_added:
        
        if port in ports:
            ports.remove(port)
    
    ports = list(map(str, ports))
    
    if len(ports) == 1:
        ports = [0]
    
    ports_added = ports[:]
    
    for port in ports_added:
        
        if port in ports:
            ports.remove(port)
    
    ports = list(map(str, ports))
    
    if len(ports) == 1:
        ports = [0]
    
    ports_added = ports[:]
    
    for port in ports_added:
        
        if port in ports:
            ports.remove(port)
    
    ports = list(map(str, ports))
    
    if len(ports) == 1:
        ports = [0]
    
    ports_added = ports[:]
    
    for port in ports_added:
        
        if port in ports:
            ports.remove(port)
    
    ports = list(map(str, ports))
    
    if len(ports) == 1:
        ports = [0]
    
    ports_added = ports[:]
    
    for port in ports_added:
        
        if port in ports:
            ports.remove(port)
    
    ports = list(map(str, port