#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers and converts fruits. """    
    
    numbers = input("Enter a number or numbers: ")
    fruits = input("Enter a fruit: ")
    
    numbers = numbers.split()
    fruits = fruits.split()
    
    numbers = [int(n) for n in numbers]
    fruits = [