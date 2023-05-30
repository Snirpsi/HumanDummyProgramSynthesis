#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi', 'grapes', 'watermelon']
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print('The fruit is', fruit)
        else:
            print('The fruit is', fruit, 'is not in the list')
