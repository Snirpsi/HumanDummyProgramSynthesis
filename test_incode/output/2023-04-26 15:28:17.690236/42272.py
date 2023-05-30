#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input or adds fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print('{} is 