#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    import sys
    
    numbers = []
    for arg in sys.argv[1:]:
        numbers.append(int(arg))
    
    numbers.sort()
    
    i = 0
    while i < len(numbers):
        if numbers[i] < numbers[i-1]:
            numbers[i] = numbers[i-1]
            