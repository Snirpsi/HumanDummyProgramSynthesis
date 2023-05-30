#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of numbers or multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        numbers = sys.argv[1:]
        
        for number in numbers:
            print(number * 2)
    else:
        print("Usage:")
        print("  python 