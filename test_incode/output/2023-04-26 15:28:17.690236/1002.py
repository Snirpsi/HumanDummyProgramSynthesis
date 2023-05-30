#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers and prints a port. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        print(convert_number(number))
    else:
        print("Usage: python3 convert_number.py <number>")
        
