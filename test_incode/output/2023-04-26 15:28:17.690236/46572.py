#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers or converts user input. """    
    while True:
        number = input('Enter a number: ')
        try:
            number = int(number)
        except ValueError:
            print('That was not a number')
        else:
            print('The number is', number * 