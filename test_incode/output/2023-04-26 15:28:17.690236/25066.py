#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    numbers = [int(i) for i in input().split()]
    
    while numbers:
        numbers.pop(0)
        
        numbers.append(int(numbers.pop(0)))
        
        print(*numbers, sep='