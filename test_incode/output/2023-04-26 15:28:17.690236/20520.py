#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers and adds a list of numbers. """    
    numbers = [int(i) for i in input("Enter a numbers: ").split()]
    numbers.extend(list(map(int, input("Enter another numbers: ").split())))
    print(numbers)

<|/ file filename=