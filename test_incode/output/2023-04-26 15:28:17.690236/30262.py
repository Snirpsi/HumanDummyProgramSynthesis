#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    import sys
    
    number = sys.argv[1]
    
    try:
        number = int(number)
    except ValueError:
        print("ERROR: Invalid number.")
        sys.exit(1)
    
    print("The number is: " + str(number))
    
