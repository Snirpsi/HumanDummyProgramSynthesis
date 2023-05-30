#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers or removes fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print('{} is in your list'.format(fruit))
        else:
            print('{} is not in your list'.format(fruit))
            
