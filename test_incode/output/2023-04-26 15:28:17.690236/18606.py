#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    
    number = sys.argv[1]
    
    try:
        number = int(number)
    except ValueError:
        print("Usage: python number_to_