#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of numbers and returns numbers. """    
    numbers = [1, 2, 3, 4, 5]
    
    for index, number in enumerate(numbers):
        print('Number {} is {}'.format(index, number))
        
    print('Done!')
    
