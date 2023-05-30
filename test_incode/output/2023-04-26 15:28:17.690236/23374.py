#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or removes fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print(fruit)
        else:
            print('No fruit found')
