#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input or prints a list of numbers. """    
    while True:
        number = input('Enter a number: ')
        if number == 'q':
            break
        elif number == '':
            print('Enter a number')
        else:
            print(number)
    
