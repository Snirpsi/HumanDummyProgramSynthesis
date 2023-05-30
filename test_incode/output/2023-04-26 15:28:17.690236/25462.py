#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or returns fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        number = int(input('Enter a number: '))
        if number > len(fruits):
            print('Sorry, the number you entered is too big.')
            continue
        else:
            print('The number you entered is {}'.format(number))
            print('The fruits are {}'.format(fruits[number]))
            
