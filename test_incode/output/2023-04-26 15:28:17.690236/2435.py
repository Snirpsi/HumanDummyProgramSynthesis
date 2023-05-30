#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers and returns a list of numbers. """    
    numbers = []
    while True:
        numbers.append(int(input('Enter a number: ')))
        print('Numbers added:', numbers)
        print('Numbers returned:', numbers)
        print('Program end