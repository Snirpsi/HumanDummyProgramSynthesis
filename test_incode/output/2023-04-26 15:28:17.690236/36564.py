#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python convert_numbers.py <number>")
        sys.exit()
    
    number = sys.argv[1]
    
    try:
        number = float(number)
    except ValueError:
        print("Usage: python convert_numbers.py <number>")
        sys.exit()
    
    print("Converted 