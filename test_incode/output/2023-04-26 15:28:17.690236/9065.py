#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits. """    
    while True:
        fruit = input('Enter fruit name: ')
        if fruit == 'quit':
            break
        else:
            print('You chose ' + fruit)
            