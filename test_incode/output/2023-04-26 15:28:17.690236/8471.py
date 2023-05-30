#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input or enumerates a list of numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            if number > 0:
                print(number)
            else:
                print('Invalid input')
        except ValueError:
            print('Invalid input')
