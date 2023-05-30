#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores all ports or opens user input. """    
    
    ports = []
    
    while True:
        ports.append(input("Enter port number: "))
        
        if len(ports) == 2:
            break
        
    if len(ports) == 1:
        ports.append(input("Enter port number: "))
        
    if len(ports) == 0:
        print("No ports found")
        
    ports.sort()
    
    ports = ports[0:2]
    
    ports_open = False
    
    for port in ports:
        if port not in ports_open:
            ports_open = True
            
            if port == "1":
                ports_open = False
                
                print("Port 1 opened")
                
            elif port == "2":
                ports_open = False
                
                print("Port 2 opened")
                
            else:
                print("Invalid port number")
                
        else:
            print("Port is already open")
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
