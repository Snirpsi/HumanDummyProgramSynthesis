#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers and removes fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        number = input('Enter a number: ')
        if number in fruits:
            print('You entered a number that 