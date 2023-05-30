#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers or prints a list of numbers. """    
    while True:
        try:
            n = int(input('Enter a number: '))
            if n < 0:
                print('Negative numbers are not allowed')
                continue
            if n == 0 or n == 1:
                print('The number you entered is 0 or 1')
                continue
            if n%2 == 0:
                print('The number you entered is even')
                continue
            if n%2 == 0:
                print('The number you entered is odd')
                continue
            break
        except ValueError:
            print('Invalid input')
            continue
    print('The number you entered is {}'.format(n))
    
