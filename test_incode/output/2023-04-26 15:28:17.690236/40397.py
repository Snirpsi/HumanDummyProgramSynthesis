#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input and converts a list of numbers. """    
    
    number = input("Enter a number: ")
    
    number = number.split()
    
    number = list(map(int, number))
    
    number = " ".join(map(str, number))
    
    print(number)
    
