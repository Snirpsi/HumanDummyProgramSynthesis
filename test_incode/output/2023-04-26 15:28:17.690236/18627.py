#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits. """    
    while True:
        fruits = input('Enter your favorite fruits: ')
        fruits = fruits.split()
        for fruit in fruits:
            print(