#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates numbers and enumerates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for fruit in fruits:
        for number in numbers:
            print(number, fruit)
            
