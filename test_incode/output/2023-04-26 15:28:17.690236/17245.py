#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers or returns a list of numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number % 2 == 0:
            print(number)
        else:
            print(number + 1)
    else:
        print(