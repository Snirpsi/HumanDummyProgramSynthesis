#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits or multiplyes a list of numbers. """    
    while True:
        fruit = input('Enter a fruit or type quit to exit: ')
        if fruit == 'quit':
            break
        else:
            print('You entered', fruit)
            print('Fruit multiplied by 