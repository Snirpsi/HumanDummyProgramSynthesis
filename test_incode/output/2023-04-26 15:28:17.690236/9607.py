#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or adds words. """    
    while True:
        number = input('Enter a number: ')
        number = int(number)
        if number < 10:
            print('The number you entered is too small.')
        elif number > 1000:
            print('The number you entered is too large.')
        else:
            print('The number you entered is correct.')
            break
    print('Goodbye.')
