#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and returns fruits. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fruits = []
    
    while True:
        fruits.append(numbers.pop(0))
        
        if numbers:
            fruits.append('...')
        else:
            break
        
    print('The fruits are {}'.format(