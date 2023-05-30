#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_multiplied = [x*y for x,y in zip(fruits, fruits[1:])]
    print(fruits_multiplied)
    
