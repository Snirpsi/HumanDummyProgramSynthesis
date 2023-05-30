#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruit = input('Enter a fruit name: ')
        if fruit in fruits:
            print('The fruit ' + fruit + ' is 