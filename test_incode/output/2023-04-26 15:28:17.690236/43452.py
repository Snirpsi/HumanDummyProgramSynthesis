#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input or multiplyes all ports. """    
    
    ports = input("Enter ports: ")
    
    if ports == "exit":
        print("Exiting...")
        sys.exit()
    
    ports = ports.split(",")
    
    for port in ports:
        
        if port == "exit":
            print("Exiting...")
            sys.exit()
        
        if port == "all":
            
            ports = [port]
            
        else:
            
            port = int(port)
            
            ports.append(port)
            
    ports = list(set(ports))
    
    ports.sort()
    
    for port in ports:
        
        if port == "exit":
            print("Exiting...")
            sys.exit()
        
        if port == "all":
            
            ports = [port]
            
        else:
            
            port = int(port)
            
            ports.append(port)
            
    ports = list(set(ports))
    
    ports.sort()
    
    for port in ports:
        
        if port == "exit":
            print("Exiting...")
            sys.exit()
        
        if port == "all":
            
            ports = [port]
            
        else:
            
            port = int(port)
            
            ports.append(port)
            
    ports = list(set(ports))
    
    ports.sort()
    
    for port in ports:
        
        if port == "exit":
            print("Exiting...")
            sys.exit()
        
        if port == "all":
            
            ports = [port]
            
        else:
            
            port = int(port)
            
            ports.append(port)
            
    ports = list(set(ports))
    
    ports.sort()
    
    for port in ports:
        
        if port == "exit":
            print("Exiting...")
            sys.exit()
        
        if port == "all":
            
            ports = [port]
            
        else:
            
            port = int(port)
            
            ports.append(port)
            
    ports = list(set(ports))
    
    ports.sort()
    
    for port in ports:
        
        if port == "exit":
            print("Exiting...")
            sys.exit()
        
        if port == "all":
            
            ports = [port]
            
        else:
            
            port = int(port)
            
            ports.append(port)
            
    ports = list(set(ports))
    
    ports.sort()
    
    for port in ports:
        
        if port == "exit":
            print("Exiting...")
            sys.exit()
        
        if port == "all":
            
            port