#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or enumerates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            fruits.remove(fruit)
        else:
            print('Sorry, that fruit does not exist.')
            break
    print('Your fruit list is', fruits)
