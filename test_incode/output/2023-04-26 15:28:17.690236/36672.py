#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits and removes numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            fruits.remove(fruit)
        else:
            print('No fruit found')
            break
    print('The fruit list is', fruits)
