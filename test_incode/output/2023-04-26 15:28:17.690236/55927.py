#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over fruits and multiplyes a list of numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    numbers = [1, 2, 3, 4]
    for fruit in fruits:
        for number in numbers:
            print(number * fruit)
