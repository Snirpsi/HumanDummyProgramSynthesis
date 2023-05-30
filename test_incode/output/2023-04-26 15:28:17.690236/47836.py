#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports or opens user input. """    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(',')
    
    for port in ports:
        
        try:
            port = int(port)
        except ValueError:
            print("Port must be an integer")
            continue
        
        if port < 0 or port > 65535:
            print("Port must be between 0 and 65535")
            continue
        
        ports[port] = port
        
    ports = list(set(ports))
    
    print("Ports:")
    for port in ports:
        print("\t", port)
    
    print("\nPorts found:")
    for port in ports:
        print("\t", port)
    
    print("\nPorts removed:")
    for port in ports:
        if port not in ports:
            print("\t", port)
    
    print("\nPorts added:")
    for port in ports:
        if port in ports:
            print("\t", port)
    
    print("\nPorts updated:")
    for port in ports:
        if port in ports:
            ports.remove(port)
            ports.append(port)
            
    print("\nPorts updated:")
    for port in ports:
        if port in ports:
            ports.remove(port)
            ports.append(port)
            
    print("\nPorts updated:")
    for port in ports:
        if port in ports:
            ports.remove(port)
            ports.append(port)
            
    print("\nPorts updated:")
    for port in ports:
        if port in ports:
            ports.remove(port)
            ports.append(port)
            
    print("\nPorts updated:")
    for port in ports:
        if port in ports:
            ports.remove(port)
            ports.append(port)
            
    print("\nPorts updated:")
    for port in ports:
        if port in ports:
            ports.remove(port)
            ports.append(port)
            
    print("\nPorts updated:")
    for port in ports:
        if port in ports:
            ports.remove(port)
            ports.append(port)
            
    print("\nPorts updated:")
    for port in ports:
        if port in ports:
            ports.remove(port)
            ports.append(port)
            
    print("\nPorts updated:")
    for port in ports:
        if port in ports:
            ports.remove(port)
            ports.append(port)
            
    print("\nPorts updated:")
    for port in ports:
        if port in ports:
            ports.remove(port)
            ports.append(port)
            
    print("\nPorts updated:")
    for port in ports: