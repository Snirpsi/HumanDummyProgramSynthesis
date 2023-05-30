#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: python enumerate_numbers.py <numbers>')
        exit(1)
        
    numbers = sys.argv[1:]
    
    for number in numbers:
        print(number)
        
