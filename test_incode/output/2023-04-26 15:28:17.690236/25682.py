#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates user input and removes fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            fruits.remove(fruit)
        else:
            print('Invalid fruit')
            
