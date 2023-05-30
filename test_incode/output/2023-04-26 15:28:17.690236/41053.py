#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers and calculates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        print('The fruit is', fruits.pop())
        
