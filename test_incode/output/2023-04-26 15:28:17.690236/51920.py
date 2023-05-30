#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers or prints fruits. """    
    fruits = ['apple', 'banana', 'orange', 'kiwi']
    fruits_multiply = []
    for fruit in fruits:
        fruits_multiply.append(int(fruit) * 2)
    print(fruits_multiply)
    
