#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    number = int(sys.argv[1])
    
    if number > 0:
        number = number - 1
    
    print(number)
    
