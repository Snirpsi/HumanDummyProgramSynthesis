#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers or multiplyes a list of numbers. """    
    
    numbers = input("Enter numbers: ")
    
    numbers = numbers.split()
    
    numbers = [int(i) for i in numbers]
    
    numbers = [x * 