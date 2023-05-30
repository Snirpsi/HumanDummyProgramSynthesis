#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    numbers = [int(x) for x in input().split()]
    numbers = [x for x in numbers if x != 0]
    numbers = list(set(numbers))
    print(numbers)
    
