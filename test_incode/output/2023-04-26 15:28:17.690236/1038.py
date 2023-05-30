#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input and converts numbers. """    
    while True:
        number = input('Enter a number: ')
        try:
            number = int(number)
        except ValueError:
            print('Invalid input')
        else:
            print('You entered', number)
            break
    print('Done')
