#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'mango', 'cherry']
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print('The fruit is', fruit)
        else:
            print('That fruit isn\'t a fruit')
