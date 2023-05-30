#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits or adds all ports. """    
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    ports = []
    
    while True:
        
        fruits.append(input('Enter a fruit: ').lower())
        
        if fruits[-1] == 'apple':
            fruits.pop()
            
        ports.append(