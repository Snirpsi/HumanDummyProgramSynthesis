#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words and multiplyes fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    fruits_multiplied = []
    for fruit in fruits:
        fruits_multiplied.append(fruit*2)
    print('The fruits:', fruits_multiplied)
    
