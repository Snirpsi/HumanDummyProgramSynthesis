#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits or returns a list of numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        fruits = input('Enter a fruit: ')
        if fruits == 'quit':
            break
        else:
            print(