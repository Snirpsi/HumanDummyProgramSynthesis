#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes fruits. """    
    fruits = ['apple', 'orange', 'banana', 'pear']
    
    for fruit in fruits:
        fruit = fruit.upper()
        
        if fruit == 'APPLE':
            print('The fruit is', fruit)
        else:
            print('The fruit is', fruit + ' 