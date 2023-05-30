#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print('{} was added to the fruit list.'.format(fruit))
        else:
            print('{} is not in the fruit list.'.format(fruit))
