#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    
    import sys
    
    numbers = []
    
    for arg in sys.argv[1:]:
        numbers.append(int(arg))
    
    numbers.sort()
    
    print(numbers)
    
    remove