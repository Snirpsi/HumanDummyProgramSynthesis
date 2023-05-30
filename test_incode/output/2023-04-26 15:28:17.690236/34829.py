#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits and returns all ports. """    
    fruits = ['apple', 'banana', 'cherry']
    ports = []
    while True:
        ports.append(fruits.pop(0))
        print(ports)
        
