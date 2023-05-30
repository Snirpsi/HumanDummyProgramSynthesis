#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input or removes numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Please try again.')
            continue
    
    if number < 0:
        print('Negative numbers are not allowed. Please try again.')
    elif number == 0:
        print('Zero is not allowed. Please try again.')
    elif number > 0:
        print('Positive numbers are not allowed. Please try again.')
    else:
        print('You entered a number!')
    
