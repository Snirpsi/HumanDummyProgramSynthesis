#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits or adds a list of numbers. """    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'quit':
            break
        else:
            print(