#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruit = input('Enter fruit name: ')
        if fruit not in fruits:
            print('{} is not in our list of fruits.'.format(fruit))
        else:
            fruits.remove(fruit)
            print('{} has been removed.