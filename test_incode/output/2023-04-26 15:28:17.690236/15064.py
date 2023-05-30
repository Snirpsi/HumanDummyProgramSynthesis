#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: enumerate <numbers>")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        print("%d: %s" % (number, number