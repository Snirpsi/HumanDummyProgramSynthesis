#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input or converts all ports. """    
    
    ports = input("Enter ports (comma separated): ")
    ports = ports.split(",")
    
    while True:
        
        ports_converted = []
        for port in ports:
            
            port_converted = int(port)
            
            if port_converted > 65535:
                port_converted = 65535
            elif port_converted < 1:
                port_converted = 1
            
            ports_converted.append(port_converted)
        
        ports_converted = list(set(ports_converted))
        
        if len(ports_converted) == 0:
            break
        
        ports_converted = ports_converted.sort()
        
        print("Ports converted: ", ports_converted)
        
        ports = input("Enter ports (comma separated): ")
        ports = ports.split(",")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
