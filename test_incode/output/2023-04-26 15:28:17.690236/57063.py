#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits. """    
    while True:
        fruits = ['apple', 'banana', 'cherry']
        fruits.append(input('Enter a fruit: '))
        print('The fruits are {}'.format(