#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    numbers = [int(i) for i in input().split()]
    
    i = 0
    
    while i < len(numbers):
        numbers[i] = numbers[i] + numbers[i+1]
        i += 1
    
    print(*numbers, sep=' ')
    
