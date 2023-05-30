#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers or enumerates user input. """    
    
    numbers = input("Enter numbers: ")
    
    if numbers.isdigit():
        numbers = [int(n) for n in numbers.split()]
    
    for number in numbers:
        print(number)
        
