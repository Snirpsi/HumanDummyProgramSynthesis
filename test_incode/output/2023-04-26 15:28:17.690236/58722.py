#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or prints words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <list>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        print(number)
    
