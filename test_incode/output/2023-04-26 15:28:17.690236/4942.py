#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of numbers or enumerates user input. """    
    
    numbers = [int(i) for i in input("Enter numbers: ").split()]
    
    for num in numbers:
        print(num)
        
