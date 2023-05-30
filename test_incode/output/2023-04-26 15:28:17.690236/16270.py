#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port and adds fruits. """    
    
    ports = input("Enter the ports: ")
    fruits = input("Enter the fruits: ")
    
    ports = ports.split()
    fruits = fruits.split()
    
    ports_fruits = zip(ports, fruits)
    
    for port, fruit in ports_fruits:
        
        if port in ports_fruits:
            
            ports_fruits.remove(port)
            
        if fruit in ports_fruits:
            
            ports_fruits.remove(fruit)
            
    
    for port, fruit in ports_fruits:
        
        if port in ports:
            
            ports.remove(port)
            
        if fruit in ports:
            
            ports.remove(fruit)
            
    
    for port, fruit in ports_fruits:
        
        if port in fruits:
            
            fruits.remove(port)
            
        if fruit in fruits:
            
            fruits.remove(fruit)
            
    
    for port, fruit in ports_fruits:
        
        if port in fruits:
            
            fruits.remove(port)
            
        if fruit in fruits:
            
            fruits.remove(fruit)
            
    
    for port, fruit in ports_fruits:
        
        if port in ports:
            
            ports.remove(port)
            
        if fruit in ports:
            
            ports.remove(fruit)
            
    
    for port, fruit in ports_fruits:
        
        if port in fruits:
            
            fruits.remove(port)
            
        if fruit in fruits:
            
            fruits.remove(fruit)
            
    
    for port, fruit in ports_fruits:
        
        if port in fruits:
            
            fruits.remove(port)
            
        if fruit in fruits:
            
            fruits.remove(fruit)
            
    
    for port, fruit in ports_fruits:
        
        if port in fruits:
            
            fruits.remove(port)
            
        if fruit in fruits:
            
            fruits.remove(fruit)
            
    
    for port, fruit in ports_fruits:
        
        if port in fruits:
            
            fruits.remove(port)
            
        if fruit in fruits:
            
            fruits.remove(fruit)
            
    
    for port, fruit in ports_fruits:
        
        if port in fruits:
            
            fruits.remove(port)
            
        if fruit in fruits:
            
            fruits.remove(fruit)
            
    
