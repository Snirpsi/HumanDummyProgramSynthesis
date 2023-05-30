#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input or multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            print('The number you entered is', number)
        else:
            print('The number you entered is', number * 2)
    else:
        print('Usage: python 