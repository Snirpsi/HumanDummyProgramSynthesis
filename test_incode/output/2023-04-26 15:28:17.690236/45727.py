#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers and returns fruits. """    
    numbers = range(1,10)
    fruits = []
    for number in numbers:
        if number % 2 == 0:
            fruits.append(number)
    print(*fruits)

<|/ file filename=