#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits or returns fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruits = convert_fruits(fruits)
        if fruits == 'quit':
            break
        else:
            print('\n'.join(