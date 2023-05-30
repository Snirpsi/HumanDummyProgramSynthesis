#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits or enumerates fruits. """    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'quit':
            break
        else:
            print('The fruit is', fruit)
            print('The fruit enumerates are:')
            for fruit in enumerate(fruit):
                print('\t', fruit)
            print('\n')
    
<|/ file ext=.py source=github |>