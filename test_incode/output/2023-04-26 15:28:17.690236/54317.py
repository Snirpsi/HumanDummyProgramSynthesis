#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 printnums.py <num>")
        exit(1)
    
    num = int(sys.argv[1])
    
    print("The number is", num)
    
