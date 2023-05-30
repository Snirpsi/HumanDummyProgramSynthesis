#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers and iterates over user input. """    
    numbers = [int(i) for i in input("Enter numbers: ").split()]
    
    for number in numbers:
        print(number * 2)
        
