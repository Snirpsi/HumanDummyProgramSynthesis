#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers and opens a list of numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    numbers = list(map(int, numbers))
    
    numbers_open = []
    
    for number in numbers:
        numbers_open.append(number)
    
    numbers_open.sort()
    
    for number in numbers_open:
        print(number)
        
