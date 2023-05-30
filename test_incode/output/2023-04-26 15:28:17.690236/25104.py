#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words and multiplyes fruits. """    
    while True:
        fruits = input('Enter your fruit names: ')
        fruits = fruits.split()
        fruits_multiplied = 0
        for fruit in fruits:
            fruits_multiplied += fruits_multipli