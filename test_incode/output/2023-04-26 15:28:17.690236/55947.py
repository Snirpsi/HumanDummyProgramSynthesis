#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits or prints a list of numbers. """    
    while True:
        fruits = input('Enter a fruit: ')
        if fruits == 'quit':
            break
        else:
            print('Fruit is', fruit