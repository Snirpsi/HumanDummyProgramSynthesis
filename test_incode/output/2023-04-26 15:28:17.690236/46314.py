#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints fruits and enumerates fruits. """    
    fruits = ['apple', 'banana', 'cherry', 'pear']
    fruits_enum = enumerate(fruits)
    for fruit, index in fruits_enum:
        print('Fruit:', fruit)
        print('Index:', index)
    print('Done.')
    
