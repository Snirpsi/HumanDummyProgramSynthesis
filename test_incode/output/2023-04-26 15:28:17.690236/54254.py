#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input or returns fruits. """    
    while True:
        fruit = input('Enter a fruit (apple, orange, pear, mango): ')
        if fruit == 'quit':
            print('Bye!')
            break
        else:
            print('You chose ' + fruit)
            print('')
            print('Your fruit 