#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input and multiplyes a list of numbers. """    
    
    numbers = input("Enter a series of numbers: ")
    
    numbers = [int(i) for i in numbers.split()]
    
    numbers = [x*y for x,y in zip(numbers, numbers[1:])]
    
    print(numbers)
    
