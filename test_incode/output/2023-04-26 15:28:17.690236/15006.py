#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates numbers. """    
    
    import sys
    
    number = int(sys.argv[1])
    
    if number < 1:
        print("No number given")
    else:
        print(number*2)
    
