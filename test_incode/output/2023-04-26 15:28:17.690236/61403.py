#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number % 2 == 0:
            print(number, 'is an even number')
        else:
            print(number, 'is an odd number')
        print('\n')
