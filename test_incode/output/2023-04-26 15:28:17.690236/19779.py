#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input or adds fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print('You already have this fruit.')
        else:
            fruits.append(fruit)
            print('Added 