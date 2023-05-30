#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        numbers = [int(i) for i in sys.argv[1:]]
        
        print(*numbers)
    else:
        print("Usage: python 