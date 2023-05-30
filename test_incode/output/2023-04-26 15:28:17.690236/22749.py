#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python numbertobinary.py <number>")
        sys.exit(1)
    
    number = sys.argv[1]
    
    binary = bin(number)
    
    print("Binary of 