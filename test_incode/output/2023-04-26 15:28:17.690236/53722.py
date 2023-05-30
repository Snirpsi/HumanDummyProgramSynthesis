#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers or removes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <number> [number]" % sys.argv[0])
        sys.exit(0)
    
    number = sys.argv[1]
    if len(sys.argv) > 2:
        number = sys.argv[2]
    
    number = int(number)
    
    if number < 0:
        print("Error: negative numbers not allowed")
        sys.exit(0)
    
    if number == 0:
        print("Error: zero numbers not allowed")
        sys.exit(0)
    
    if number > sys.maxsize:
        print("Error: number too big")
        sys.exit(0)
    
    if number < -sys.maxsize:
        print("Error: number too small")
        sys.exit(0)
    
    if number == int(number):
        print("Error: number not an integer")
        sys.exit(0)
    
    if number == float(number):
        print("Error: number not an 