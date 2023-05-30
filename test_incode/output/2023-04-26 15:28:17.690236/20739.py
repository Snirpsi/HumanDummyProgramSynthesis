#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers. """    
    while True:
        number = input('Enter a number: ')
        if number == 'done':
            print('Thanks for playing!')
            break
        else:
            print(number)
