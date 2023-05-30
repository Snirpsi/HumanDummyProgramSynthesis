#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input or opens a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 numbers.py")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        print(number)
    
