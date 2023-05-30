#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers. """    
    numbers = input("Enter a number: ")
    numbers = numbers.split()
    numbers = list(map(int, numbers))
    numbers.sort()
    print(numbers)
    
