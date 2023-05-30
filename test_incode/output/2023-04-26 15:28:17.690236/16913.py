#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits and calculates a list of numbers. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi']
    fruits_numbers = []
    for fruit in fruits:
        fruits_numbers.append(len([x for x in fruits if x == fruit]))
    print(fruits_numbers)
