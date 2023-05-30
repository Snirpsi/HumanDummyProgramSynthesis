#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input and multiplyes a list of numbers. """    
    
    numbers = input("Enter a list of numbers: ")
    
    numbers = [int(x) for x in numbers.split()]
    
    total = 0
    
    for number in numbers:
        total += number
    
    print(total)
    
