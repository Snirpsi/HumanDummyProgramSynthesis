#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers. """    
    numbers = input("Enter a list of numbers: ")
    numbers = [int(n) for n in numbers.split()]
    
    numbers_converted = []
    for number in numbers:
        numbers_converted.append(number * 2)
    
    print(numbers_converted)
    
