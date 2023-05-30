#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits. """    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'quit':
            break
        print('You entered', fruit)
        print('