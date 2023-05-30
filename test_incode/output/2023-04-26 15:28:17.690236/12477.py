#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python remove_numbers.py <numbers>")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    remove_numbers(numbers)
    
