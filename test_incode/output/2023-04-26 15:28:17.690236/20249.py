#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates numbers. """    
    
    numbers = [
        int(i) for i in input().split()
    ]
    
    sum = 0
    
    for number in numbers:
        sum += number
    
    print(sum)
    
