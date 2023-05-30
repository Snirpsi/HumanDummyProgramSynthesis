#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers and calculates fruits. """    
    
    fruits = []
    
    while True:
        number = int(input("Enter a number: "))
        fruits.append(number)
        
        if number == 