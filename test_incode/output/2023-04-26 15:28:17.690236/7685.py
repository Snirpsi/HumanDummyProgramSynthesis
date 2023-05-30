#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers and multiplyes a list of numbers. """    
    while True:
        number = int(input('Enter a number: '))
        numbers = [number] * int(input('Enter a number of times to multiply: '))
        print('The product is: ', numbers)
