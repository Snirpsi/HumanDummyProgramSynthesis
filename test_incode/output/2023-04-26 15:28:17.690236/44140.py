#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers. """    
    
    import sys
    
    numbers = []
    
    for arg in sys.argv[1:]:
        numbers.append(int(arg))
    
    for n in numbers:
        print(n)
        
