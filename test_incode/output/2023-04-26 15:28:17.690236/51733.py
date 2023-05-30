#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes fruits and returns a list of numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    numbers = []
    for fruit in fruits:
        numbers.append(int(fruit) * 2)
    print(numbers)
