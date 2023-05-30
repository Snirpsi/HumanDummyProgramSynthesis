#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 convert_numbers.py <numbers>")
        sys.exit()
    
    numbers = [int(n) for n in sys.argv[1].split(',')]
    
    numbers_str = ','.join(str(n) for n in numbers)
    
    print("The numbers {} are {}.".format(numbers_str, numbers_str))
    
