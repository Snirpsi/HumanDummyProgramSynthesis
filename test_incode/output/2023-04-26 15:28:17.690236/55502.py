#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers or removes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = int(input("Enter a number: "))
    
    