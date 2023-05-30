#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers and multiplyes user input. """    
    
    numbers = input("Enter a number: ")
    
    numbers = numbers.split()
    
    numbers = [int(x) for x in numbers]
    
    numbers = [x * 