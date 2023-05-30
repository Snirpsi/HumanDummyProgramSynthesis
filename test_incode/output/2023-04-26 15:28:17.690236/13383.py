#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates numbers or returns numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python enumerate_numbers.py')
        sys.exit()
    
    numbers = enumerate_numbers(sys.argv[1])
    
    for number in numbers:
        print(number)
        
