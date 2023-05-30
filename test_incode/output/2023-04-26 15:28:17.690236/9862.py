#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers. """    
    numbers = []
    while True:
        number = int(input('Enter a number: '))
        if number in numbers:
            print('That number has already been entered.')
        else:
            numbers.append(number)
            print('The entered number is', number)
            print('The list of numbers is', numbers)
            print('')
            print('Press any key to exit.')
            