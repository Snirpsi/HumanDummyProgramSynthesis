#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates fruits and converts all ports. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    ports = ['1', '2', '3', '4']
    fruits_ports = enumerate(fruits, ports)
    
    for fruit, port in fruits_ports:
        print("Fruit: " + fruit + " Port: " + port)
