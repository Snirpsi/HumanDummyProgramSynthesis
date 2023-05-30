#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers or multiplyes numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Please enter a number')
            
    print('The product of %d and %d is %d.' % (number, number, number*number))
    
