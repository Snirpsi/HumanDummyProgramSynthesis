#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input or multiplyes a list of numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = 1
    
    numbers = [int(i) for i in sys.argv[2:]]
    
    for number in numbers:
        print(number * number)
        
