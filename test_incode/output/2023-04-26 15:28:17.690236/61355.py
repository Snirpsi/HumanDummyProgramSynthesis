#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        print(number * number)
        
