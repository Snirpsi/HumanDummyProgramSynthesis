#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or enumerates numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        numbers = sys.argv[1:]
    else:
        numbers = range(1,100)
    
    for number in numbers:
        print(number)
        
