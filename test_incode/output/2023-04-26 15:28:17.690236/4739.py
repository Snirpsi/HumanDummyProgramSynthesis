#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input and removes numbers. """    
    while True:
        number = input('Enter a number: ')
        try:
            number = float(number)
        except ValueError:
            print('Invalid input. Please enter a number.')
            continue
        if number > 0 and number < 10:
            print('The number you entered is {}.'.format(number))
        else:
            print('Invalid input. Please enter a number between 1 and 10.')
            continue
        break
    print('Goodbye!')
