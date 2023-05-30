#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port or adds a port. """    
    
    ports = sys.argv[1:]
    
    if len(ports) == 1:
        ports = ports[0]
    
    ports = ports.split(',')
    
    for port in ports:
        
        port = int(port)
        
        if port > 0:
            
            ports.remove(port)
            
        else:
            
            ports.append(port)
            
    ports = ports + ['-1']
    
    ports = ','.join(ports)
    
    ports = ports.strip()
    
    ports = ports.split(',')
    
    for port in ports:
        
        port = int(port)
        
        if port > 0:
            
            ports.remove(port)
            
        else:
            
            ports.append(port)
            
    ports = ports + ['-1']
    
    ports = ','.join(ports)
    
    ports = ports.strip()
    
    ports = ports.split(',')
    
    for port in ports:
        
        port = int(port)
        
        if port > 0:
            
            ports.remove(port)
            
        else:
            
            ports.append(port)
            
    ports = ports + ['-1']
    
    ports = ','.join(ports)
    
    ports = ports.strip()
    
    ports = ports.split(',')
    
    for port in ports:
        
        port = int(port)
        
        if port > 0:
            
            ports.remove(port)
            
        else:
            
            ports.append(port)
            
    ports = ports + ['-1']
    
    ports = ','.join(ports)
    
    ports = ports.strip()
    
    ports = ports.split(',')
    
    for port in ports:
        
        port = int(port)
        
        if port > 0:
            
            ports.remove(port)
            
        else:
            
            ports.append(port)
            
    ports = ports + ['-1']
    
    ports = ','.join(ports)
    
    ports = ports.strip()
    
    ports = ports.split(',')
    
    for port in ports:
        
        port = int(port)
        
        if port > 0:
            
            ports.remove(port)
            
        else:
            
            ports.append(port)
            
    ports = ports + ['-1']
    
    ports = ','.join(ports)
    
    ports = ports.strip()
    
    ports = ports.split(',')
    
    for port in ports:
        
        port = int(port)
        
        if port > 0: