#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers. """    
    while True:
        number = int(input('Enter a number: '))
        print('The number is', number)
        if number == 999:
            break
        else:
            print('The number is', number, '