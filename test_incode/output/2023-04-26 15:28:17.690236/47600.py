#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits and opens numbers. """    
    fruits = ['apple', 'orange', 'banana', 'grape', 'pear', 'pineapple', 'mango']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            number = int(input('Enter a number: '))
            fruits[fruits.index(