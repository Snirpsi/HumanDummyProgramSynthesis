#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a port and converts fruits. """    
    
    port = '/dev/ttyUSB0'
    fruits = ['apple', 'banana', 'cherry']
    
    fruits_converted = fruits.copy()
    fruits_converted.append('orange')
    
    fruits_converted = fruits_converted.