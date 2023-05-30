#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers or iterates over user input. """    
    
    number = int(input('Enter a number: '))
    
    if number > 10:
        print('The number you entered is too large.')
    elif number < 0:
        print('The number you entered is too small.')
    else:
        print('The number you entered is ' + str(number))
    
