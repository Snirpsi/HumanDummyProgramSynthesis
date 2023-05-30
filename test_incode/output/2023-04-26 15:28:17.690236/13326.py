#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        print(number * 2)
    else:
        print("Usage: python 