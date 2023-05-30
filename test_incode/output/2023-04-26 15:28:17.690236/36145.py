#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers. """    
    numbers = [1, 2, 3, 4, 5]
    for index, num in enumerate(numbers):
        print('{}. {}'.format(index, num))
    print('')
    print('