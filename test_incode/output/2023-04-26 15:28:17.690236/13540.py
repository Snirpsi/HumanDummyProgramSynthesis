#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words or enumerates fruits. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi']
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print('The fruit is', fruit)
        else:
            print('The fruit is', fru