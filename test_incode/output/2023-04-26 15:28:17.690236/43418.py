#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input and returns numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number > 100 or number < 1:
            print('Invalid number')
        else:
            print(number)
