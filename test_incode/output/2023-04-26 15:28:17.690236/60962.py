#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    numbers = sys.argv[1:]
    numbers = list(map(int, numbers))
    numbers.sort()
    numbers.reverse()
    numbers = numbers[: