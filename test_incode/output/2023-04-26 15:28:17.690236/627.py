#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes user input and iterates over a list of numbers. """    
    numbers = [int(i) for i in input("Enter a numbers: ").split()]
    
    for number in numbers:
        print(number * 2)
        
