#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input and converts user input. """    
    while True:
        line = input('Enter a number: ')
        try:
            number = int(line)
        except ValueError:
            print('Invalid input')
        else:
            break
    print('You entered', number, '