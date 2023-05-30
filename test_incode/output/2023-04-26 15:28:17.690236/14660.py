#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits or iterates over fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print(fruit)
        else:
            print('That fruit does not exist!')
