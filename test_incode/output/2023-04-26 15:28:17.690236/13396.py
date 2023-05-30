#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    import sys
    
    number = sys.argv[1]
    
    try:
        number = int(number)
    except ValueError:
        print("Error: %s is not a number" % number)
    else:
        print("The number is", number)
    
