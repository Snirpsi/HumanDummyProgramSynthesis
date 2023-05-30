#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and multiplyes numbers. """    
    numbers = []
    while True:
        number = int(input('Enter a number: '))
        if number in numbers:
            print('That number is already in the list')
        else:
            numbers.append(number)
            print('The number is', number*