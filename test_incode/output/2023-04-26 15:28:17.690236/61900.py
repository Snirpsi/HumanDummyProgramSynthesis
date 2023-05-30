#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <number>" % sys.argv[0])
        sys.exit()
    
    number = int(sys.argv[1])
    
    numberStr = str(number)
    
    numberStr = "{0:.{1}f}".format(number, 