#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for index, num in enumerate(numbers):
        print('{}. {}'.format(index, num))
    
    print('Done.')
    
