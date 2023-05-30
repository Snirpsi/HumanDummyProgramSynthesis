#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print(