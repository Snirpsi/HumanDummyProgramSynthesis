#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or opens user input. """    
    while True:
        number = int(input('Enter a number: '))
        if number < 1:
            print('Invalid number')
        elif number > 10:
            print('Too high')
        else:
            print('You entered a number!')
            break
