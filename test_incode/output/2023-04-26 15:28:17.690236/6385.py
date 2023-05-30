#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port or removes all ports. """    
    ports = sys.argv[1:]
    if len(ports) == 1:
        ports = [0]
    
    ports = ports.split(',')
    
    for port in ports:
        port_number = int(port)
        
        port_to_remove = port_number - 1
        
        if port_to_remove < 0:
            port_to_remove = 0
        
        port_to_remove = port_to_remove % len(ports)
        
        port_to_remove = port_to_remove + 1
        
        port_to_remove = port_to_remove % len(ports)
        
        port_to_remove = port_to_remove + 1
        
        port_to_remove = port_to_remove % len(ports)
        
        port_to_remove = port_to_remove + 1
        
        port_to_remove = port_to_remove % len(ports)
        
        port_to_remove = port_to_remove + 1
        
        port_to_remove = port_to_remove % len(ports)
        
        port_to_remove = port_to_remove + 1
        
        port_to_remove = port_to_remove % len(ports)
        
        port_to_remove = port_to_remove + 1
        
        port_to_remove = port_to_remove % len(ports)
        
        port_to_remove = port_to_remove + 1
        
        port_to_remove = port_to_remove % len(ports)
        
        port_to_remove = port_to_remove + 1
        
        port_to_remove = port_to_remove % len(ports)
        
        port_to_remove = port_to_remove + 1
        
        port_to_remove = port_to_remove % len(ports)
        
        port_to_remove = port_to_remove + 1
        
        port_to_remove = port_to_remove % len(ports)
        
        port_to_remove = port_to_remove + 1
        
        port_to_remove = port_to_remove % len(ports)
        
        port_to_remove = port_to_remove + 1
        
        port_to_remove = port_to_remove % len(ports)
        
        port_to_remove = port_to_remove + 1
        
        port_to_remove = port_to_remove % len(ports)
        
        port_to_remove = port_to_remove + 1
        
        port_to_remove = port_to_remove % len(ports)
        
        port_to_remove = port_to_remove + 1
        
        port_to_remove = port_to_remove % len(ports)
        
        port_to_remove = port_to_remove + 1
        
        port_to_remove = port_to_remove % len(ports)
        