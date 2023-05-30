#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of numbers or converts numbers. """    
    
    # enumerate a list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, number in enumerate(numbers):
        print('Number: ', index, 'Value: ', number)
    
    # convert numbers to strings
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, number in enumerate(numbers):
        print('Number: ', index, 'Value: ', str(number))
    
    # convert numbers to floats
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, number in enumerate(numbers):
        print('Number: ', index, 'Value: ', float(number))
    
    # convert numbers to integers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, number in enumerate(numbers):
        print('Number: ', index, 'Value: ', int(number))
    
    # convert numbers to booleans
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, number in enumerate(numbers):
        print('Number: ', index, 'Value: ', bool(number))
    
    # convert numbers to tuples
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, number in enumerate(numbers):
        print('Number: ', index, 'Value: ', tuple(number))
    
    # convert numbers to lists
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, number in enumerate(numbers):
        print('Number: ', index, 'Value: ', list(number))
    
    # convert numbers to dictionaries
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, number in enumerate(numbers):
        print('Number: ', index, 'Value: ', dict(number))
    
    # convert numbers to sets
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, number in enumerate(numbers):
        print('Number: ', index, 'Value: ', set(number))
    
    # convert numbers to frozensets
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, number in enumerate(numbers):
        print('Number: ', index, 'Value: ', frozenset(number))
    
    # convert numbers to frozendicts
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, number in enumerate(numbers):
        print('Number: ', index, 'Value: ', frozendict(number))
    
    # convert numbers to frozenlists
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, number in enumerate(numbers):
        print('Number: ', index, 'Value: ', frozenlist(number))
    
    # convert numbers to sets of frozensets
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, number in enumerate(numbers):
        print('Number: ', index, 'Value: ', frozenset(frozenset(number)))
    
    # convert numbers to sets of frozendicts
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, number in enumerate(numbers):
        print('Number: ', index, 'Value: ', frozendict(frozendict(number)))