#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_converted = []
    
    while True:
        fruits_converted.append(input('Enter a fruit (type "quit" to quit): '))
        
        if fruits_converted[-1] == 'quit':
            break
        
        fruits_converted.append(fruits_converted[-1]