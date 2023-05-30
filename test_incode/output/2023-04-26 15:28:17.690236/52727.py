#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input and removes numbers. """    
    while True:
        number = input('Enter a number: ')
        if number.isdigit():
            print(number)
        else:
            break
