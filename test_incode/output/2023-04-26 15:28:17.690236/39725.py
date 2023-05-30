#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input and returns a list of numbers. """    
    
    number = input("Enter a number: ")
    
    numbers = []
    
    for char in number:
        numbers.append(int(char))
    
    print(numbers)
    
