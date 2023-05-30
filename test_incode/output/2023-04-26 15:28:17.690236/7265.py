#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input and converts user input. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Try again.')
            
    print('The product of %d and %d is %d.' % (number, number, number * number))

<|/ file filename=