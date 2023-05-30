#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python multiply.py <number>")
        sys.exit()
    
    number = float(sys.argv[1])
    
    result = number * number
    
    print("The result is", result)
    
