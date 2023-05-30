#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words or iterates over a list of numbers. """    
    
    numbers = input("Enter a number: ")
    
    if numbers.isdigit():
        numbers = [int(numbers)]
        
    for number in numbers:
        print(number)
    
