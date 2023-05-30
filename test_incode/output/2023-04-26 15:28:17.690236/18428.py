#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python multiply.py <number>")
        sys.exit()
    
    number = sys.argv[1]
    
    print("The result is:", number * 2)
    
