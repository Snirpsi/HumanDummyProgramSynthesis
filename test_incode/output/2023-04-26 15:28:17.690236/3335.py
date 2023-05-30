#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    while True:
        fruit = input('What would you like to add? ')
        if fruit in fruits:
            print(fruit + ' is added to your 