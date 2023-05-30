#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number % 2 == 0:
            print("{} is an even number.".format(number))
        else:
            print("{} is an odd number.".format(number))
    else:
        print("Usage: python 