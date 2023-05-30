#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s number" % sys.argv[0])
        exit(1)
    
    number = sys.argv[1]
    
    for n in range(number):
        print("%d" % n)
    
