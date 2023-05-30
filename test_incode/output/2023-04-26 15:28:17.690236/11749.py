#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number > 1000:
            print('Too high!')
        elif number < 1:
            print('Too low!')
        else:
            print('You entered a number!')
            break
