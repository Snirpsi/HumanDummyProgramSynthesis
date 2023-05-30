#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits and enumerates a list of numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_enumerated = enumerate(fruits)
    for index, fruit in fruits_enumerated:
        print('Fruit #{} is {}'.format(index, fruit))
    
