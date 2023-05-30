#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits or removes a list of numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    numbers = [1, 2, 3, 4]
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print('The fruit ' + fruit + ' is ' + fruits[fruits.index(