#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers or stores words. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            print(number)
        else:
            print("No number given")
    else:
        print("Usage: python enumerate.py <number>")
    
