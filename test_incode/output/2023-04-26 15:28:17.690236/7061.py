#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers. """    
    
    import sys
    
    number = sys.argv[1]
    
    count = 0
    
    for digit in str(number):
        count += 1
    
    print(count)
    
