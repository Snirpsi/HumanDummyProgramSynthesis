#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates user input and calculates all ports. """    
    
    ports = []
    
    for port in ports:
        
        if port == '':
            
            port = 'COM' + str(port)
            
        ports.append(port)
        
    ports = list(set(ports))
    
    ports.sort()
    
    for port in ports:
        
        