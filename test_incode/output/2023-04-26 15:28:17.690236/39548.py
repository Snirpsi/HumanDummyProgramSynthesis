#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or stores a list of numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            if number > 0 and number < 10:
                print(number)
            else:
                print('Invalid input')
        except ValueError:
            print('Invalid input')
        else:
            break
