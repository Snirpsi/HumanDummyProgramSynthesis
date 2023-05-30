#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers and removes user input. """    
    
    numbers = input("Enter numbers: ")
    
    numbers = [int(n) for n in numbers.split(",")]
    
    numbers = [n for n in numbers if n != 0]
    
    numbers = list(set(numbers))
    
    print(numbers)
    
