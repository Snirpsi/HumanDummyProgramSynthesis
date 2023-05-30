#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and removes numbers. """    
    numbers = []
    while True:
        numbers.append(int(input('Enter a number: ')))
        if numbers[-1] == numbers[0]:
            break
        else:
            print('Numbers 