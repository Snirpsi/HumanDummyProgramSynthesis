#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers and removes fruits. """    
    
    numbers = input("Enter numbers: ")
    fruits = input("Enter fruits: ")
    
    fruits = fruits.split()
    
    numbers = numbers.split()
    
    numbers = [int(n) for n in numbers]
    
    fruits = [