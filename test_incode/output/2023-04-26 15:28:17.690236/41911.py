#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input and converts numbers. """    
    while True:
        number = input('Enter a number: ')
        try:
            number = int(number)
        except ValueError:
            print('That was not a number!')
        else:
            print('The number you entered was', number)
            
