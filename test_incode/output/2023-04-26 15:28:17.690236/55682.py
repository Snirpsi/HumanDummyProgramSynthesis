#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes fruits and converts a port. """    
    fruits = ['apple', 'banana', 'orange', 'pear']
    fruits_port = ['apple', 'banana', 'orange', 'pear', 'apple', 'banana', 'orange', 'pear']
    fruits_port_converted = [fruit, fruits_port[i] * fruits_port[i + 1] for i in range(len(fruits_port) - 1)]
    print(fruits_port_converted)
    
