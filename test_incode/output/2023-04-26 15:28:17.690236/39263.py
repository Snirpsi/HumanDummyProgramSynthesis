#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    numbers = [int(i) for i in input().split()]
    
    while True:
        numbers.append(int(input()))
        
        if numbers[-1] == numbers[-2]:
            break
        
    print(*numbers, sep='