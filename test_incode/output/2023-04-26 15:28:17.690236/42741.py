#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        print('You have {} fruits.'.format(len(fruits)))
        print('Which one would you like to add?')
        fruit = input('> ')
        if fruit in fruits:
            print('{} is already in use, try again'.format(fruit))
        else:
            fruits.append(fruit)
            print('{} has been added'.format(fruit))
