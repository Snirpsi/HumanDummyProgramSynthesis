#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'grape']
    fruits_multiplied = []
    
    for fruit in fruits:
        fruits_multiplied.append(fruit*2)
    
    print('The fruits that multiplied are:')
    print(fruits_multiplied)
    
