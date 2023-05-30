#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers and returns fruits. """    
    fruits = []
    while True:
        fruits.append(int(input('Enter a number: ')))
        if fruits[-1] == 999:
            break
    print('The fruits are {}'.format(