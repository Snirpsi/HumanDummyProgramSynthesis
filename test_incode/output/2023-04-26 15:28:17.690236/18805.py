#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits and iterates over a list of numbers. """    
    fruits = ['apple', 'banana', 'orange', 'kiwi']
    fruits_iter = enumerate(fruits)
    for fruit, number in fruits_iter:
        print('{} has {} apples.'.format(fruit, number))
