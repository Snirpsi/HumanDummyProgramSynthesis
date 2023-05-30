#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers and multiplyes a list of numbers. """    
    numbers = [int(i) for i in input().split()]
    numbers = [x*y for x, y in zip(numbers, numbers[1:])]
    print(numbers)
    
