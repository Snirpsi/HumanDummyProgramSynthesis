#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits and opens a list of words. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    words = ['apples', 'oranges', 'bananas', 'cherries']
    
    while True:
        fruits_multiplied = []
        for fruit in fruits:
            fruits_multiplied.append(fruit*