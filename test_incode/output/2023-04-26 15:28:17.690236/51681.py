#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers. """    
    
    import sys
    
    numbers = sys.stdin.readlines()
    
    for number in numbers:
        print(int(number))
    
