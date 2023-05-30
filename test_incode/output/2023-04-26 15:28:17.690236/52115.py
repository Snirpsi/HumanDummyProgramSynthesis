#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    while True:
        fruit = 'apple'
        while fruit not in fruits:
            fruit = input('Please input a fruit: ')
        fruit = fruits[fruits.index(