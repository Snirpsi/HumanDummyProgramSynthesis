#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    import sys
    numbers = sys.argv[1:]
    numbers = [int(x) for x in numbers]
    numbers.sort()
    numbers = numbers[:]
    numbers.reverse()
    numbers = numbers[: