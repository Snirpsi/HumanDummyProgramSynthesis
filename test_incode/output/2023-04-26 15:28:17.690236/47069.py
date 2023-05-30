#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits and calculates user input. """    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        fruits_multiplied = [0] * len(fruits)
        
        for fruit in fruits:
            fruits_multiplied[fruit] = int(fruit) * 