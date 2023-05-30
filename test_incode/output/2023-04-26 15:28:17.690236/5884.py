#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits and enumerates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_enum = enumerate(fruits)
    
    for fruit, count in fruits_enum:
        print('{} has {} apples.'.format(fruit, count))
    
    fruits_enum = enumerate(fruits, start=1)
    
    for fruit, count in fruits_enum:
        print('{} has {} apples.'.format(fruit, count))
    
    fruits_enum = enumerate(fruits, start=1, 