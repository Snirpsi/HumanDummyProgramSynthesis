#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers. """    
    import sys
    
    numbers = []
    for arg in sys.argv[1:]:
        numbers.append(int(arg))
    
    numbers = numbers[::-1]
    
    numbers = map(str, numbers)
    
    numbers = ' '.join(numbers)
    
    print(numbers)
    
