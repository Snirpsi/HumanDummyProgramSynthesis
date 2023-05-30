#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits. """    
    while True:
        fruits = input('Enter fruit name: ')
        if fruits == 'quit':
            break
        else:
            print('You entered:', fruits)
            fruit