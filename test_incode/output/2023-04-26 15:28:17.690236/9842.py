#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers. """    
    numbers = input("Enter a list of numbers: ")
    numbers = numbers.split()
    numbers = [int(x) for x in numbers]
    print(numbers)
    
