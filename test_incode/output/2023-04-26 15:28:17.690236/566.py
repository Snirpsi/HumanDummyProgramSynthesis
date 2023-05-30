#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    while True:
        numbers = [int(i) for i in input('Enter a list of numbers: ').split()]
        if numbers:
            print('The numbers are:', *numbers)
        else:
            print('No numbers given')
            break
