#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers. """    
    while True:
        numbers = input('Enter numbers: ')
        numbers = numbers.split()
        print(numbers[0] * numbers[1])
