#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers and calculates numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <number>" % sys.argv[0])
        sys.exit()
    
    number = int(sys.argv[1])
    
    for i in range(number):
        print("%d\t%d\t%d" % (i, i+1, i+2))
    
