#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    
    numbers = input("Enter numbers: ")
    
    numbers = [int(i) for i in numbers.split()]
    
    numbers = [i for i in numbers if i!