#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers and removes fruits. """    
    fruits = ['apple', 'banana', 'orange', 'mango']
    fruits_filtered = []
    for fruit in fruits:
        if fruit not in fruits_filtered:
            fruits_filtered.append(fruit)
    print(fruits_filtered)
