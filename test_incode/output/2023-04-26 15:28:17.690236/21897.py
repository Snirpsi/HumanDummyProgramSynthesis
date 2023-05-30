#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers and enumerates user input. """    
    
    import sys
    
    numbers = list(map(int, sys.stdin.readline().split()))
    
    enumerated_numbers = []
    
    for number in numbers:
        enumerated_numbers.append(number)
        
    print(enumerated_numbers)
    
