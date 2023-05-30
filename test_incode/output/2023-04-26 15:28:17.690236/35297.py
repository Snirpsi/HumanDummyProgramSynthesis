#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    while True:
        number = input('Enter a number: ')
        try:
            number = int(number)
        except ValueError:
            print('That is not a number')
        else:
            break
    
    numbers = list(range(number))
    
    numbers.reverse()
    
    print('The numbers 