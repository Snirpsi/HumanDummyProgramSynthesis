#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or calculates numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Please enter a number')
            continue
    
    if number % 2 == 0:
        print('{} is an even number.'.format(number))
    else:
        print('{} is an odd number.'.format(number))
    
