#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input and prints a list of numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number < 0:
            print('Negative numbers not allowed')
        elif number > 0:
            print('Positive numbers not allowed')
        else:
            print(number)
