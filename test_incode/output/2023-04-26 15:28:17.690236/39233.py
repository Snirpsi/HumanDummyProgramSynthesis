#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or calculates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print('The fruit ' + fruit + ' is ' + fruits[fruits.index(