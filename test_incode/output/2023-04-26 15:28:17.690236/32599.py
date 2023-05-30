#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        multiplier = 1
        for fruit in fruits:
            multiplier = multiplier * fruit
        print(fruit