#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports or enumerates a list of numbers. """    
    
    ports = openports()
    
    if ports:
        ports = list(ports)
        
        ports.sort()
        
        ports = ports[2:]
        
        ports = list(map(lambda port: str(port), ports))
        
        ports.sort()
        
        print(ports)
        
    else:
        print("No ports found")
        
