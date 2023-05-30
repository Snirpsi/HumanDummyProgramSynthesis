#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: python3 convert.py <number>')
        sys.exit()
    
    number = int(sys.argv[1])
    
    if number < 0:
        print('Error: number cannot be negative.')
        sys.exit()
    
    number