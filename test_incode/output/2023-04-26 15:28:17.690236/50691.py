#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over numbers and multiplyes fruits. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fruits = ['apple', 'banana', 'cherry']
    for number in numbers:
        for fruit in fruits:
            print(number * fruit)
    
