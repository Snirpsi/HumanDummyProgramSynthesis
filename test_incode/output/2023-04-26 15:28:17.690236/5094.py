#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number < 1:
            print('Invalid number')
        elif number > 100:
            print('Invalid number')
        else:
            print('The number is', number)
            break
    
