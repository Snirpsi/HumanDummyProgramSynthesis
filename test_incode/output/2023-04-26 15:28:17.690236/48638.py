#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python %s number" % sys.argv[0])
        exit(1)
    
    number = sys.argv[1]
    
    print("The product of %d is %d" % (number, number * 