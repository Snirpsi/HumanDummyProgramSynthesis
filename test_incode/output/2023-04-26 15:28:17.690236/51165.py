#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits and adds user input. """    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'quit':
            break
        else:
            print('You entered ' + fruit)
            