#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    
    numbers = [int(i) for i in input().split()]
    
    sum = 0
    for i in numbers:
        sum += i
    
    print(sum)
    
