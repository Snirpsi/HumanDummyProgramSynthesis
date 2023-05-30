#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input and removes user input. """    
    while True:
        line = input('Enter a number: ')
        try:
            number = int(line)
        except ValueError:
            print('That is not a valid number')
            continue
        else:
            print('You entered', number, '