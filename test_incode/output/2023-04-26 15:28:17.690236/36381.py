#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'cherry']
    while True:
        print('Current fruits:', fruits)
        print('Enter a fruit:')
        fruit = input()
        if fruit in fruits:
            print('You already have that fruit.')
        else:
            fruits.append(fruit)
            print('Added new fruit:', fruit)
            print('Current fruits:', fruits)
            print('')
