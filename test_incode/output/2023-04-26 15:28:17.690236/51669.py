#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits. """    
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    fruits_sum = 0
    
    for fruit in fruits:
        fruits_sum += fruit
    
    print('The sum of all fruits is {}.'.format(fruits_sum))
    
