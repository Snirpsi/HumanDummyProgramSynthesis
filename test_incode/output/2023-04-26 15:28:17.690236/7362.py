#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers. """    
    while True:
        number = int(input('Enter a number: '))
        number = number * 2
        print('The product of {} and {} is {}'.format(number, number, number * 2))
        
