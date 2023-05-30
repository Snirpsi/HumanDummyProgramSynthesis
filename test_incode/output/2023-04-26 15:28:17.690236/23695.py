#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    import sys
    
    number = sys.argv[1]
    
    number = int(number)
    
    if number > 0:
        number = number - 1
        
        print(number)
    else:
        print("Number cannot be negative.")
        
