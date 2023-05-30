#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers and prints fruits. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fruits = ['apple', 'banana', 'cherry']
    
    for number in numbers:
        print(number, 'is', fruits[number])
        
