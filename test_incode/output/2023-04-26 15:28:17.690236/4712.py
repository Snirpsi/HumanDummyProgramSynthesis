#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers or prints numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        print(number)
    else:
        print("Usage: python 