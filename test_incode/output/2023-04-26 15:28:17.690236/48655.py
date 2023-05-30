#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
        except ValueError:
            print('Invalid input')
        else:
            print('The number you entered is', number)
            break
    print('Ending program')
