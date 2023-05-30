#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits or multiplyes fruits. """    
    fruits = ['apple', 'banana', 'orange']
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print('{} is {}x'.format(fruit, fruits[fruit]))
        else:
            print('{} is not in our list of fruits.'.format(fruit))
