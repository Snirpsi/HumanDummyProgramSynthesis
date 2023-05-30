#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over fruits and enumerates all ports. """    
    fruits = ['apple', 'banana', 'cherry']
    ports = []
    for fruit in fruits:
        ports.append(enumerate(fruit))
    print(ports)
    
