#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers. """    
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    numbers = [int(n) for n in numbers]
    
    print(numbers)
    
