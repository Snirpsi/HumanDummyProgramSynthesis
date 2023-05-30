#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python print_numbers.py <numbers>")
        exit(1)
    
    numbers = map(int, sys.argv[1].split(","))
    
    for number in numbers:
        print(number)
        
