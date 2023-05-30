#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits or enumerates a list of numbers. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        number = input('Enter a number: ')
        
        if number in fruits:
            print('The fruit is', fruits[number])
        else:
            print('The fruit is', fruits.index('