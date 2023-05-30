#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers or prints numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number1 = int(sys.argv[1])
        number2 = int(sys.argv[2])
        
        print(number1 * number2)
    else:
        print("Usage: python 