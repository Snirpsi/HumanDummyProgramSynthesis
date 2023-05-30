#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns fruits and enumerates a port. """    
    fruits = ['apple', 'banana', 'cherry']
    ports = [80, 81]
    
    fruits_ports = enumerate(fruits, ports)
    
    for fruit, port in fruits_ports:
        print('{0} is on port {1}'.format(fruit, port))
    
