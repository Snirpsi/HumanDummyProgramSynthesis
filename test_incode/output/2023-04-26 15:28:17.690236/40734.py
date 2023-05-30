#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates user input or removes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            print('The number is', number)
        else:
            print('The number is', number, '