#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of numbers and calculates fruits. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi', 'grape', 'mango']
    fruits.sort()
    for fruit in fruits:
        print("{} = {}".format(fruit, fruits[fruit]))
