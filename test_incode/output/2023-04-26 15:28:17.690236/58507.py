#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits or adds user input. """    
    while True:
        fruit = input('Enter a fruit name: ')
        if fruit == 'quit':
            print('Goodbye')
            break
        else:
            print('You entered', fruit)
            print('