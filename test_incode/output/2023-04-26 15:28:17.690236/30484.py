#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers or multiplyes user input. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Try again.')
    
    while True:
        try:
            multiplier = int(input('Enter a multiplier: ')) * number
            break
        except ValueError:
            print('Invalid input. Try again.')
    
    print('The product is', number, 'x', multiplier)
    
