#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints fruits or returns user input. """    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print('The fruit is ' + fruit)
        else:
            print('The fruit is unknown')
        
