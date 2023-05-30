#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words and multiplyes fruits. """    
    words = ['apple', 'banana', 'orange', 'kiwi']
    fruits = ['apple', 'banana', 'orange', 'kiwi', 'mango']
    
    words = [x for x in words if x != '']
    fruits = [x for x in fruits if x != '']
    
    fruits_multiply = []
    
    for fruit in fruits:
        fruits_multiply.append(fruit*