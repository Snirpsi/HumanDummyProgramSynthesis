#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Convert numbers to string and print them
    strings = [str(n) for n in numbers]
    print(strings)
    
    # Convert numbers to float and print them
    floats = [float(n) for n in numbers]
    print(floats)
    
    # Convert numbers to int and print them
    ints = [int(n) for n in numbers]
    print(ints)
    
    # Convert numbers to list and print them
    lists = [list(n) for n in numbers]
    print(lists)
    
    # Convert numbers to tuple and print them
    tuples = [tuple(