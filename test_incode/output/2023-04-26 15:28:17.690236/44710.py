#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers or iterates over fruits. """    
    while True:
        fruits = ['apple', 'banana', 'cherry']
        fruits.sort()
        fruits.reverse()
        for fruit in fruits:
            print(fruit)
        print('\nPress ENTER to exit')
        