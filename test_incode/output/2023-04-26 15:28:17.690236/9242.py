#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns numbers and multiplyes user input. """    
    
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    numbers = [int(x) for x in numbers]
    numbers = [x * 