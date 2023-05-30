#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python %s <list.txt>" % (sys.argv[0]))
        sys.exit()
    
    with open(sys.argv[1]) as f:
        numbers = [int(i) for i in f]
    
    numbers_converted = [number