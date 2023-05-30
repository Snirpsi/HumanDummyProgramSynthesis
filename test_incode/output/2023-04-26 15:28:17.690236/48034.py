#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes fruits. """    
    fruits = ['apple', 'banana', 'orange', 'mango']
    fruits_multiplied = [x*y for x,y in zip(fruits,fruits)]
    print(fruits_multiplied)
