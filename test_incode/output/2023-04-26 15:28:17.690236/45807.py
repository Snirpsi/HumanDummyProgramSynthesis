#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input. """    
    while True:
        line = input('Enter a number: ')
        try:
            number = int(line)
            break
        except ValueError:
            print('Invalid input. Please try again.')
            continue
    print('You entered', number, '