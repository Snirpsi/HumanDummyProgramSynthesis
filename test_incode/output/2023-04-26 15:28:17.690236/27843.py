#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers or multiplyes user input. """    
    while True:
        number = int(input('Enter a number: '))
        if number == 0: break
        print('The number is', number, 'multiplied by 