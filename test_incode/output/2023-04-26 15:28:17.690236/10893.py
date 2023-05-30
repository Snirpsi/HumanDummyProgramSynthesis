#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over fruits and opens all ports. """    
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    for fruit in fruits:
        
        ports = openPorts(fruit)
        
        for port in ports:
            
            port.close()
            
