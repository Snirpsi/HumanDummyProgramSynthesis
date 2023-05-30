#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits. """    
    fruits = ['apple', 'banana', 'orange', 'mango']
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print('You chose ' + fruit)
        else:
            print('Sorry, I do not know ' + fruit)
