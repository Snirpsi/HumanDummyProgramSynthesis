#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers. """    
    numbers = sys.argv[1:]
    numbers = map(int, numbers)
    numbers = list(numbers)
    numbers.sort()
    print(numbers)
    
