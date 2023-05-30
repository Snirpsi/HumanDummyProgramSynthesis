#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds fruits or removes all ports. """    
    
    fruits = ['apple', 'orange', 'banana']
    
    # Remove all ports
    ports = fruits.copy()
    ports.remove('apple')
    
    # Add all ports
    fruits.extend(ports)
    
    print(fruits)
    
