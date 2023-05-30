#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers and returns user input. """    
    while True:
        number = int(input('Enter a number: '))
        if number == -1:
            print('Goodbye!')
            break
        else:
            print('You entered', number)
            print('