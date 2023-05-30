#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    import sys
    numbers = sys.argv[1:]
    numbers = list(map(int, numbers))
    numbers.sort()
    numbers.reverse()
    numbers = list(filter(lambda x: x not in numbers, numbers))
    print(numbers)
