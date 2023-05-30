#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds numbers. """    
    numbers = [int(x) for x in input().split()]
    numbers.append(sum(numbers))
    print(*numbers, sep='