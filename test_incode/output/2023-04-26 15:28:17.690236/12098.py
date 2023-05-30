#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers or prints user input. """    
    while True:
        number = int(input('Enter a number: '))
        if number == 0: break
        print('The product of {} and {} is {}'.format(number, number * 2, number * 3))
        
