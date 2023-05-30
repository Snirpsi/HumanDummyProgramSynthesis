#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits. """    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'apple':
            print('You chose apple')
        elif fruit == 'orange':
            print('You chose orange')
        else:
            print('You chose something else')
