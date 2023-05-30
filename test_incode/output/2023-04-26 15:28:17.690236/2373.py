#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input. """    
    while True:
        try:
            user_number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Try again.')
    
    print('You entered', user_number, '