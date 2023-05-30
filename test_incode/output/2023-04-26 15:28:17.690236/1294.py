#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes fruits or opens a list of words. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    fruits_multiply = []
    
    for fruit in fruits:
        fruits_multiply.append(fruit*2)
        
    print(fruits_multiply)
    
    fruits_open = []
    
    for fruit in fruits:
        fruits_open.append(fruit+'