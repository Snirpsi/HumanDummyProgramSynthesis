#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or prints a list of numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            print('The number is', number)
        else:
            print('The number is', number, '