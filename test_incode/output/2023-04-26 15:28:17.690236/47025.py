#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number == 999:
            print('Thanks for playing!')
            break
        else:
            print('The number is', number)
