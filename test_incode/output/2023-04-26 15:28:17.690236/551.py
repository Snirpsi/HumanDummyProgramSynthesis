#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of numbers. """    
    numbers = []
    while True:
        number = int(input('Enter a number: '))
        if number == 0:
            break
        numbers.append(number)
    print('The numbers 