#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers or iterates over a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = 1
    
    for x in range(number):
        print(x)
    
