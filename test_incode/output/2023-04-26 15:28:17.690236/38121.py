#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers. """    
    while True:
        number = input('Enter a number: ')
        try:
            number = int(number)
        except ValueError:
            print('Invalid number')
        else:
            if number < 0 or number > 100:
                print('Invalid number')
            else:
                