#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers. """    
    while True:
        number = input('Enter a number: ')
        if number == 'done':
            print('Thanks for playing!')
            break
        else:
            print('You entered', number)
