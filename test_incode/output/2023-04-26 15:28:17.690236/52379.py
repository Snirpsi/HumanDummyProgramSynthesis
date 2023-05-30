#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of numbers or multiplyes numbers. """    
    import sys
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        if number > 0:
            print(number * 2)
        else:
            print("No numbers to multiply")
    else:
        print("Usage: python list.py <number>")
    
