#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits or adds fruits. """    
    while True:
        fruit = input('Enter a fruit name: ')
        if fruit == 'quit':
            break
        else:
            print('You entered ' + fruit)
            