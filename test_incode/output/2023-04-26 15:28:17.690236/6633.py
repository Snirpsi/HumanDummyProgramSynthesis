#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over fruits and returns user input. """    
    fruits = ['apple', 'banana', 'orange', 'pear', 'grape']
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print('The fruit is', fruit)
        else:
            print('The fruit is', fruit, 'is not in the list')
